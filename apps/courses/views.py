# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course


class CourseListView(View):
    """
    课程列表页
    """

    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_courses.order_by("-students")
        elif sort == 'hot':
            all_courses = all_courses.order_by("-click_nums")

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)

        org_nums = all_courses.count()

        return render(request, "course-list.html", {
            'all_courses': courses,
            "sort": sort,
            'hot_courses': hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums +=1
        course.save()

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            # 模板中用 for 循环，所以要传入数组，即使是空数组
            relate_courses = []

        return render(request, "course-detail.html", {
            'course': course,
            'relate_courses': relate_courses
        })
