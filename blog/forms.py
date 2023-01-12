from django.db import models
from .models import PostArticle, ArticleComments, ArticleLikes
from django.forms import ModelForm
from django import forms


class AddArticleForm(ModelForm):

    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={'placeholder': 'Title'}), max_length=200)
    article_image = forms.ImageField(required=False)
    content = forms.CharField(label="Content", widget=forms.Textarea(
        attrs={'placeholder': 'insert description here'}))

    class Meta:
        model = PostArticle
        fields = ['title', 'content', 'article_image',]

        # widgets = {
        #     "title": forms.TextInput(attrs={'placeholder': 'Title', "class": "form-control"}),
        #     "content": forms.Textarea(attrs={'placeholder': 'Content', "class": "form-control content"}),
        #     "article_image": forms.FileInput(attrs={'placeholder': 'Image', "class": "form-control"}),
        #     "author": forms.HiddenInput,
        # }


class CommentForm(ModelForm):

    class Meta:
        model = ArticleComments
        fields = ("article", "author", "content",)

        widgets = {
            "article": forms.HiddenInput(),
            "author": forms.HiddenInput(),
            "content": forms.Textarea(attrs={"class": "form-control content"}),
        }


class AddComment(ModelForm):
    content = forms.CharField(label="Comment", widget=forms.TextInput(
        attrs={'placeholder': 'Enter a Comment'}))

    class Meta:
        model = ArticleComments
        fields = ['content']

# class UpdateArticleForm(ModelForm):
#     title = forms.CharField(label="Title", widget=forms.TextInput(
#         attrs={'placeholder': 'Title'}), max_length=200)
#     article_image = forms.ImageField(required=False)
#     description = forms.CharField(label="Content", widget=forms.Textarea(
#         attrs={'placeholder': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'}))

#     class Meta:
#         model = PostArticle
#         fields = ['title', 'article_image', 'description']


# class AddComment(ModelForm):
#     content = forms.CharField(label="Comment", widget=forms.TextInput(
#         attrs={'placeholder': 'Enter a Comment'}))

#     class Meta:
#         model = ArticleComments
#         fields = ['content']
