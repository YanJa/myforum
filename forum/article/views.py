# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from block.models import Block
from .models import Article
# Create your views here.


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_obj = Article.objects.filter(block=block, status=0)
    return render(request, "article_list.html", {"articles": article_obj, "b": block})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request, "article_create.html",
                          {"error": "标题和内容都不为空",
                           "b": block})
        if len(title) >10 or len(content) > 100:
            return render(request, "article_create.html",
                          {"error": "标题或内容太长了",
                           "title": title,
                           "content": content,
                           "b": block})
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" % block_id)
