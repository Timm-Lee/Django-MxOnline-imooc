# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

import xadmin

from users.views import LoginView


urlpatterns = [
    # xadmin 后台管理页面
    url(r'^xadmin/', xadmin.site.urls),

    # 主页
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    # 用户登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 用户登录post
]