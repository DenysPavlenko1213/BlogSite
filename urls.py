from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('article-details/<int:pk>', views.article_details, name='article-details'),
    path('post-article', views.post_article, name='post-article')
]
