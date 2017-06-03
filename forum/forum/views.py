from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User

def index(request):
    # block_info = Block.objects.all().order_by("-id")
    block_info = Block.objects.filter(status=0).order_by("-id")
    return render(request, "index.html", {"blocks": block_info})


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        user.is_active = True
        

    return render(request, "register.html")
