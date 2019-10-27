from django.shortcuts import render
from block.models import Block

# Create your views here.


# 首页查询出所有版块信息
def index(request):
    res = Block.objects.filter(status=0).order_by("-id")
    return render(request, "index.html", {"block_info": res, "user": request.user.username})
