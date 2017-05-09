# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/9/17 12:01 PM'

from django.conf.urls import url

from .views import UserInfoView, UploadImageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
]

