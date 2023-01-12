from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.base import TemplateView


from .models import PostArticle, ArticleComments
from .forms import AddArticleForm, CommentForm, AddComment, ArticleLikes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


# def home_page(request):
#     # article_list = PostArticle.objects.all().order_by('-date_created')

#     return render(request, 'blog/homepage.html')


class HomeView(TemplateView):
    template_name = "blog/homepage.html"

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs).context_data
        context["articles"] = PostArticle.objects.all()
        # import pdb
        # pdb.set_trace()
        return self.render_to_response(context)


class DashboardView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated():
            blog = PostArticle.objects.all().order_by('-date_created')

            return render(request, 'blogs/homepage.html', {'blog': blog})
        else:
            return redirect('users:login')


def add_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = {'author': request.user}
            form = AddArticleForm(request.POST, request.FILES, initial=data)
            if form.is_valid():
                addArticle = form.save(commit=False)
                addArticle.author = request.user
                form.save()
                return redirect('blog:homepage')
        else:
            form = AddArticleForm()

        return render(request, 'blog/addarticle.html', {'form': form})
    else:
        return redirect('users:login')


def comment_add(request, article_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            commentForm = AddComment(request.POST)
            if commentForm.is_valid():
                article = get_object_or_404(PostArticle, pk=article_id)
                addComment = commentForm.save(commit=False)
                addComment.author = request.user
                addComment.article = article
                commentForm.save()
            return redirect('')


class viewArticleView(TemplateView):

    def get(self, *args, **kwargs):
        viewArticle = PostArticle.objects.all(pk=self.kwargs['article_id'])
        return render(self.request, 'blog/viewArticle.html', {'viewArticle': viewArticle})


def add_article_comment(request, article_id):
    form = PostArticle.objects.filter(pk=article_id)
    instance = get_object_or_404(PostArticle, pk=article_id)
    commentForm = AddComment()
    loadComment = ArticleComments.objects.filter(
        article=instance).order_by('date_published')
    if request.user.is_authenticated:
        likes = ArticleLikes.objects.filter(
            article=instance, owner=request.user)
        totallikes = ArticleLikes.objects.filter(
            article=instance, likebool=True).count()
        return render(request, 'blog/viewarticle.html', {'form': form,
                                                         'commentForm': commentForm, 'loadComment': loadComment, 'likes': likes,
                                                         'totallikes': totallikes})
    else:
        return render(request, 'blog/viewarticle.html', {'form': form,
                                                         'commentForm': commentForm, 'loadComment': loadComment})
