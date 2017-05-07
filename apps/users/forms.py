# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 8:50 AM'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


# 登录表单验证，加入了验证码
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

# 找回密码
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})