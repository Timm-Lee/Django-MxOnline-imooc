# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/8/17 11:17 AM'

from django.conf.urls import url
from .views import CourseListView, CourseDetailView


urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程列表页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

]