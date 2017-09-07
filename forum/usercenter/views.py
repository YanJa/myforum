from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import UserForm
from forum.secret import EMAIL_HOST_USER
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile  # 用户配置文件库
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # 接收表单数据
            username = form.cleaned_data['username']
            userresult = User.objects.filter(username=username)
            email = form.cleaned_data['email']
            if userresult:
                return render_to_response("usercenter/register.html", {"errors": "用户名已存在",
                                                                       "username": username,
                                                                       "email": email})
            else:
                password = form.cleaned_data['password']
                re_password = form.cleaned_data['re_password']

                if password != re_password:
                    return render_to_response('usercenter/register.html', {'errors': "两次密码不一致",
                                                                           "username": username,
                                                                           "email": email})

                # 创建用户
                user = User.objects.create_user(username, email, password)
                user.is_active = False  # 激活用户并保存
                user.save()

                # 邮箱设置
                import uuid
                user_code = str(uuid.uuid4()).replace("-", "")
                active_link = "http://%s/active/%s" % (request.get_host(), user_code)
                active_email = '点击<a href="%s">这里</a>激活' % active_link
                active_info = "用户%s注册成功,已发送激活邮件至您的邮箱，请去邮箱查看邮件并激活您的账号" % username
                send = send_mail(subject='[Select]激活邮件',
                                 message='点击链接激活%s' % active_link,
                                 html_message=active_email,
                                 from_email=EMAIL_HOST_USER,
                                 recipient_list=[email],
                                 fail_silently=False)
                if send:
                    now = timezone.now()
                    overdue_time = now - timedelta(seconds=600)
                    user_profile = UserProfile(username=username,
                                               active_code=user_code,
                                               overdue_time=overdue_time)
                    user_profile.save()
                # 返回注册成功页面
                return render_to_response('usercenter/success.html', {'active_info': active_info})
    else:
        form = UserForm()
    return render_to_response("usercenter/register.html", {"form": form})


def login(request):
    pass


def active(request):
    pass
