# Django 顺序3：用户注册



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





## 验证码包 django-simple-captcha==0.4.6

### 注册到 settings 

放入 INSTALLED_APPS

```python
INSTALLED_APPS = [
    #...
    'captcha',
]
```

配置路由 urls.py。

```python
from django.conf.urls import url, include
urlpatterns = [
    # 验证码图片的路由
    url(r'^captcha/', include('captcha.urls')),
]
```

makemigrations/migrate 之后，在数据库中出现表名叫“captcha_captchastore”。

注意路由中不能带`$`，因为是include，需要留给包含的其他路由地址用，还不能用`$`结束。

不能写成：

```python
    url(r'^captcha/$', include('captcha.urls')),
```





### 定义带验证码字段的 form

注意这里不是 `form.CaptchaField()`。

```python
from captcha.fields import CaptchaField
# 登录表单验证，加入了验证码
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
```



### get 请求时，把 register_form 返回到模板中

注意这里 `RegisterForm()` 中不需要带参数，因为不做验证。

```python
from .forms import RegisterForm
# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})
```





### html 模板中引用 captcha 验证码

首先在 views 逻辑中实例化，再返回给模板。最后在模板中调用。就可以打开调试看到验证码出来。点击验证码区域会更换验证码。

```python
<div class="form-group marb8 captcha1 errorput">
    <label>验&nbsp;证&nbsp;码</label>
    {{ register_form.captcha }}
</div>
```

django-simple-captcha 包自己实现了 html 代码。其中包含一段属性为 hidden 的输入框，这是 captcha 生成的 hash key，name 是 `captcha_0`。而用户输入的是 input 的 name 是 `captcha_1`。最终这两个字段都会返回服务器，captcha 包在 captcha 表中进行对比核实。

```html
<div class="form-group marb8 captcha1 errorput">
    <label>验&nbsp;证&nbsp;码</label>
    <img src="/captcha/image/04599e1d3def39ef70b21cb48326d5882d919447/" alt="captcha" class="captcha" /> <input id="id_captcha_0" name="captcha_0" type="hidden" value="04599e1d3def39ef70b21cb48326d5882d919447" required /> <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" required />
</div>
```



### post逻辑中，验证 captcha

需要把 request.POST 放入 form 实例化的参数中。

```python
# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass
```



### 自定义 form 表单错误文字（以中文显示）

captcha的表单错误是英文的内容，显示

```html
<li>Invalid CAPTCHA</li>
```

在 form 中自定义成中文内容，修改字段参数 errors_messages，该参数的值是一个字典，修改其中的 invalid。

```python
class RegisterForm(forms.Form):
    #...
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})
```



### 保存用户注册信息到数据库

逻辑顺序：

* 取出 post 表单中的数据
* 实例化一个 model （数据库的表）
* 把表单数据保存到实例化的 model 中（最后是`.save()`）

这里的注意点是，密码不能以明文保存进数据，需要先用 auth.hasers 中 `make_password` 方法将用户输入的密码加密以后，再保存进数据库。

另外，由于是邮箱注册，所以该注册用户的用户名与邮箱都是用户输入的邮箱。

```python
from django.contrib.auth.hashers import make_password

# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
```



























