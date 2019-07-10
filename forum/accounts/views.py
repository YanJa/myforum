from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

from .utils import check_email
# Create your views here.


class LoginView(View):
    """
    登录视图
    """
    template = "accounts/login.html"

    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.errors = {
                "msg": ""
            }

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        """
        登录提交表单
        :param request:
        :return:
        """
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            print("用户不存在", username)
            self.errors.update({"msg": "用户不存在: %s" % username})
            return render(request, self.template, {"errors": self.errors})
        if check_password(password, user_obj.password):
            auth_login(request, user_obj)
            print("正在登录")
            return redirect('/')
        else:
            print("登录失败")
            return render(request, self.template)


class RegisterView(View):
    """
    用户注册视图
    """
    template = "accounts/register.html"

    def __init__(self, **kwargs):
        super(RegisterView, self).__init__(**kwargs)
        self.errors = {
                "msg": ""
        }

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        form = {
            "username": username,
            "email": email,
            "password": password
        }
        if password != re_password:  # 用户密码校验
            self.errors.update({"msg": "两次输入用密码不一致"})
            return render(request, self.template, {"form": form, "errors": self.errors})
        if not check_email(email):
            self.errors.update({"msg": "输入的邮箱不正确"})
            return render(request, self.template, {"form": form, "errors": self.errors})
        try:
            user_obj = User.objects.create_user(**form)
            if user_obj:
                auth_login(request, user_obj)
                print("创建用户成功")
                return redirect("/")
        except Exception as e:
            print(e)
        return render(request, self.template, {"form": form, "errors": self.errors})


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    html = "accounts/logout.html"
    auth_logout(request)
    return render(request, html)


class UserInfoView(View):
    """
    用户个人主页视图
    """
    template = "accounts/userinfo.html"

    def __init__(self, **kwargs):
        super(UserInfoView, self).__init__(**kwargs)
        self.errors = {
                "msg": ""
        }

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        form = {
            "username": username,
            "email": email,
            "password": password
        }
        if password != re_password:  # 用户密码校验
            self.errors.update({"msg": "两次输入用密码不一致"})
            return render(request, self.template, {"form": form, "errors": self.errors})
        if not check_email(email):
            self.errors.update({"msg": "输入的邮箱不正确"})
            return render(request, self.template, {"form": form, "errors": self.errors})
        try:
            user_obj = User.objects.create_user(**form)
            if user_obj:
                auth_login(request, user_obj)
                print("创建用户成功")
                return redirect("/")
        except Exception as e:
            print(e)
        return render(request, self.template, {"form": form, "errors": self.errors})
# end
