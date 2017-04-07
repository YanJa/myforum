# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.core.paginator import Paginator
from block.models import Block
from .models import Article
from .forms import ArticleForm
# Create your views here.
ARTICLE_CNT_1PAGE = 1


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no", "1"))

    # 最简单的方式实现，在地址栏添加get参数
    # start_index = (page_no - 1) * ARTICLE_CNT_1PAGE
    # end_index = page_no * ARTICLE_CNT_1PAGE
    # article_obj = Article.objects.filter(block=block, status=0).order_by("-id")[start_index:end_index]

    # 使用Paginator分页器方式
    all_articles = Article.objects.filter(block=block, status=0).order_by("-id")
    p = Paginator(all_articles, ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    article_obj = page.object_list

    page_cnt = p.num_pages
    current_no = page_no
    page_links = [i for i in range(page_no-5, page_no + 6) if 0 < i <= p.num_pages]
    previous_link = page_links[0] - 1
    nex_link = page_links[-1] + 1

    return render(request, "article_list.html", {"b": block,
                                                 "articles": article_obj,
                                                 "page": page,
                                                 "page_cnt": page_cnt,
                                                 "current_no": current_no,
                                                 "page_links": page_links,
                                                 "previous_link": previous_link,
                                                 "next_link": nex_link})


class ArticleCreateView(View):
    """基于类的控制器"""
    template_name = "article_create.html"

    def init_data(self, block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {"b": self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.status = 0
            article.save()
            return redirect("article/list/%s" % self.block_id)
        else:
            return render(request, self.template_name, {"b": self.block, "form": form})


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "a"


# 使用了基于类的view，所以基于函数的view可以不用
"""
def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():  # 判断参数合法性
            # article = Article(block=block,
            #                   title=form.cleaned_data["title"],  # 获取合法参数
            #                   content=form.cleaned_data["content"], status=0)
            article = form.save(commit=False)  # commit决定是否存入数据库
            article.block = block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:  # 出错时将form传回页面
            return render(request, "article_create.html", {"b": block, "form": form})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article_detail.html", {"a": article}) """
