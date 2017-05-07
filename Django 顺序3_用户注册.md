# Django 顺序3：用户登录



## 基础搭建

### 路由配置 urls.py

```python
from users.views import LoginView, RegisterView

urlpatterns = [
    # 用户注册
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
```



### 逻辑业务 users.views.py

```python
# 用户登录
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
```



### 模板页面 templates.register.html

增加引用静态文件。

```html
{% load staticfiles %}
```





























