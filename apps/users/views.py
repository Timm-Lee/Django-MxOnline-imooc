# coding:utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile


# 自定义 authenticate 实现邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户在 model 中是否存在，用 get 可以确保只有一个该用户
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 传入的密码，与 model 中的对比，只能使用 check_password 方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None





# 登录逻辑
def user_login(request):
    # POST 要大写
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html")
        pass
    elif request.method == 'GET':
        return render(request, 'login.html', {})
