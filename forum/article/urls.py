# -*- coding:utf-8 -*-
from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'list/(?P<block_id>\d+)/$', views.article_list),
    url(r'create/(?P<block_id>\d+)/$', views.ArticleCreateView.as_view()),
    # url(r'detail/(?P<article_id>\d+)', views.article_detail),
    url(r'detail/(?P<pk>\d+)/$', views.ArticleDetailView.as_view()),
]