# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/8/17 11:17 AM'

from django.conf.urls import url
from .views import CourseListView


urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list")

]