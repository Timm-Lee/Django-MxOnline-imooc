# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 8:50 AM'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)





