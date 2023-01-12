from django.db import models
from django.utils import timezone
from users.models import User
from django.db.models import Count
from django.conf import settings


# Create your models here.


class PostArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(
        upload_to='articleImage/', null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleComments(models.Model):
    content = models.TextField()
    article = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article.title + " : " + self.content

    def number_of_comments(self):
        return Count(self.id)


class ArticleLikes(models.Model):
    likebool = models.BooleanField()
    article = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article.title + " : " + self.author.get_short_name()

    def number_of_likes(self):
        return Count(self.id)
