from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AccountsForm
# Create your views here.


def login(request):
    pass


def register(request):
    template = "accounts/register.html"
    if request.method == 'GET':
        return render(request, template)
    else:
        print(request.POST)
        form = AccountsForm(request.POST)
        if form.is_valid():
            accounts = form.save(commit=False)  # 是否提交数据
            accounts.save()
            return redirect("/")
        else:
            response = {
                "form": form
            }
            return render(request, template, response)
