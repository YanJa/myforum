from django.shortcuts import render
from block.models import Block


def index(request):
    # block_info = [{"name": "Go专区", "desc": "go语言学习", "manager": "select"},
    #               {"name": "Python专区", "desc": "python语言学习", "manager": "select1"},
    #               {"name": "Docker专区", "desc": "docker容器学习", "manager": "select2"},
    #               {"name": "Django专区", "desc": "django基础学习", "manager": "select3"},
    #               ]
    block_info = Block.objects.all().order_by("-id")
    return render(request, "index.html", {"blocks": block_info})
