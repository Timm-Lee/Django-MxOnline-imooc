# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/6/17 11:06 AM'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile


# xadmin的配置
class BaseSetting():
    # 可以使用主题
    enable_themes = True
    # 使用bootswatch提供的主题
    use_bootswatch = True


class GlobalSettings():
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    # 每个 app 下 model 可以收缩起来
    menu_style = 'accordion'



class EmailVerifyRecordAdmin():
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin():
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)