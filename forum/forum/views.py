from django.shortcuts import render
from block.models import Block

# Create your views here.

def index(request):
    ##res = [
    #        {"name": "pandas专区", "desc": "10分钟入门pandas", "manager": "admin"},
    #        {"name": "numpy专区", "desc": "numpy学习理解", "manager": "admin"},
    #        {"name": "django专区", "desc": "django中间件怎么玩", "manager": "view"},
    #        {"name": "pytho", "desc": "python yield 怎样return返回值", "manager": "admin"}]
    res = Block.objects.all().order_by("-id")

    return render(request, "index.html", {"block_info": res})
