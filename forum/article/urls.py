"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import (
    article_list,
    #article_create,
    #article_detail,
    AticleCreateView,
    ArticleDetailView
    )


urlpatterns = [
    # 文章列表页面
    url(r'^list/(?P<block_id>\d+)', article_list, name='article_list'),
    #url(r'^create/(?P<block_id>\d+)', article_create, name='article_create'),
    #url(r'^detail/(?P<article_id>\d+)', article_detail, name='article_detail'),
    # 创建文章接口
    url(r'^create/(?P<block_id>\d+)', AticleCreateView.as_view(), name='article_create'),
    # 文章详情接口
    url(r'^detail/(?P<pk>\d+)', ArticleDetailView.as_view(), name='article_detail'),
]
