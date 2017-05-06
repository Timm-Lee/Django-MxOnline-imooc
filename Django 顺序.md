# Django 顺序



## 测试 MySQL 连接

makemigration/migrate



## 建立 apps

### users

#### 自定义 auth_user (扩展该表)

**users.models.py**

继承 AbstractUser，并增加自己扩展的字段。

  ```python
  from django.contrib.auth.models import AbstractUser

  class UserProfile(AbstractUser):
      #...
  ```

注册 AUTH_USER_MODEL 到 settings.py 中

  ```python
  AUTH_USER_MODEL = "users.UserProfile"
  ```

如果 makemigrations/migrate users 报错：

```python
Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
```

则删除 users.migrations 中的 0001_initial.py，另外删除数据库内容，再 makemigrations/migrate users。



把 app 注册到 settings 中的 installed_apps。



### 把 app 放到一个文件下（apps）

项目中新建 package (自带`__init__.py` 文件)，把所有app拖入该目录下。

注意点：去掉 PyCharm 弹出警告框中的选项： Search for references。

让 Django 直接使用 apps 的名字，而不用类似于 apps.users 的包名。

1、PyCharm 中把 apps 右键 Mark Dictionary as > Source Root

2、settings.py 中把 apps 加入python的搜索目录下。

```python
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```



### 设置 python 模板

Preferences / Editor / File and Code Templates / Python Script

```python
# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '$DATE $TIME'
```



### 把 models 注册到 xadmin 中

每个 apps 中建立 adminx.py 文件。

并把 xadmin 放入全局 urls

```python
# -*- coding:utf-8 -*-

from django.conf.urls import url
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]
```





### xadmin的全局配置

放在一个 adminx.py 中，可以放 users 中

```python


# xadmin的配置
class BaseSetting():
    # 可以使用主题
    enable_themes = True
    # 使用bootswatch提供的主题
    use_bootswatch = True


class GlobalSettings():
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'
    
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
```



配置每个 app 在 xadmin 中的显示名字，在每个 app  的目录下修改 apps.py。以Course 中的 apps.py 举例

```python
# coding:utf-8
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    verbose_name = "课程管理"
```

并在 Course 目录下的 `__init__.py` 中写入：

```python
default_app_config = "courses.apps.CoursesConfig"
```



## 静态文件处理

静态文件都放在项目目录下的 /static/ 目录中。

在 settings.py 中配置：

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

在模板中引用

```python
{% load staticfiles %}
```





## 用户登录逻辑

### index

把 index.html 放入 templates 目录中。

配置 urls

```python
#...
from django.views.generic import TemplateView

urlpatterns = [
	#...
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
]
```



#### 处理模板及静态文件：

1、引入静态文件

```html
{% load staticfiles %}
```

2、模板中引用

```python
src="{% static 'images/top_down.png' %}"
```



#### 登录逻辑处理

urls

```python
# -*- coding:utf-8 -*-

from users.views import login


urlpatterns = [
    #...

    # 用户登录页面
    url(r'^login/$', login, name='login'),  
]
```



users.views

```python
# coding:utf-8

from django.shortcuts import render
def login(request):
    # POST 要大写
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'index.html', {})
```



#### django 从 request.POST 中获取用户名与密码

```python
		user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
```



#### 认证方法 authenticate

```python
from django.contrib.auth import authenticate


user = authenticate(user_name, pass_word)
```

anthenticate 传入两个参数 username和密码，如果认证成功会返回user的model的对象，如果失败返回 None。



判断用户认证成功后，调用login，传入 request, user两个参数。跳转到首页。

```python
        if user is not None:
            login(request, user)
            return render(request, "index.html")
```



### 模板中判断是否登录 request.user.is_authenticated

用于修改首页修改右上角的头

```python
            {% if request.user.is_authenticated %}
                <!--登录后跳转-->
        	{% else %}
                <!--登录前-->
            {% endif %}
```













