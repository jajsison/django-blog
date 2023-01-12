from django.urls import path

from . import views
from .views import HomeView, viewArticleView


app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    # path('', views.home_page, name="homepage"),
    path('article/add', views.add_article, name="add_article"),
    path('article/add/comment/<int:pk>',
         views.add_article_comment, name="add_article_comment"),
    path('article/viewArticle/<int:pk>',
         views.viewArticleView.as_view(), name="article_details"),


    # path('article/list', PostList.as_view(), name="post_list"),


]
