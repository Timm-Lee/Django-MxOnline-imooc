# coding:utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login(request):
    # POST 要大写
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        pass
    elif request.method == 'GET':
        return render(request, 'login.html', {})
