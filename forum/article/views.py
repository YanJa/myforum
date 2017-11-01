from django.shortcuts import render
from .models import Article
from block.models import Block

# Create your views here.

def article_list(request, block_id):
    template = "article_list.html"
    block_id = int(block_id)
    bl = Block.objects.get(id=block_id)
    # 指定版块对应的文章信息
    article_obj = Article.objects.filter(block=bl, status=0).order_by('-id')
    response = {
        "bl": bl,
        "articles": article_obj
    }
    return render(request, template, response)
