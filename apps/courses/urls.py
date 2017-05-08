# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/8/17 11:17 AM'

from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseInfoView, ComentsView


urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程列表页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 课程列表页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', ComentsView.as_view(), name="course_comments"),


]