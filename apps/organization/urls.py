# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 4:56 PM'

from django.conf.urls import url
from .views import OrgView

urlpatterns = [
    # 课程机构列表页
    url(r'list/$', OrgView.as_view(), name="org_list"),

    #
    url(r'add_ask/$', )
]