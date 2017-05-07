# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 4:31 PM'

from django import forms


class UserAskForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=20)
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    course_name = forms.CharField(required=True, min_length=5, max_length=50)



