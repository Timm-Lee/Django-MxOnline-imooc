# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 4:31 PM'

from django import forms
from operation.models import UserAsk


# 用户提交咨询表单的验证
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']



