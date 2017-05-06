# coding:utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate


def login(request):
    # POST 要大写
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'login.html', {})
