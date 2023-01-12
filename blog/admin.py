from django.contrib import admin
from .models import PostArticle, ArticleComments, ArticleLikes

# Register your models here.


admin.site.register(PostArticle)
admin.site.register(ArticleComments)
admin.site.register(ArticleLikes)
