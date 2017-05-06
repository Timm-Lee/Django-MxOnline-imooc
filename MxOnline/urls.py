# -*- coding:utf-8 -*-

from django.conf.urls import url

import xadmin


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]