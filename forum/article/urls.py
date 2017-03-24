# -*- coding:utf-8 -*-
from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'list/(?P<block_id>\d+)', views.article_list),
    url(r'create/(?P<block_id>\d+)', views.article_create)
]
