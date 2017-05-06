# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

import xadmin


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
]