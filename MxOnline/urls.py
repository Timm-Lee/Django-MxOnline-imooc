# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import TemplateView

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView


urlpatterns = [
    # xadmin 后台管理页面
    url(r'^xadmin/', xadmin.site.urls),

    # 主页
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    # 用户登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 用户注册
    url(r'^register/$', RegisterView.as_view(), name='register'),

    # 验证码图片的路由
    url(r'^captcha/', include('captcha.urls')),

    # 用户注册：激活链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

]