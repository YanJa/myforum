from django.shortcuts import render

# Create your views here.

def article_list(request, block_id):
    block_id = int(block_id)
    return render(request, "article/article_list.html")
