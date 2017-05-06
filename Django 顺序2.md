# Django 顺序2



### 自定义 authenticate() 实现邮箱登录

在 user.views 中自定义 authenticate 方法（重载），这里是只考虑传入用户名和密码的情况。

成功就返回 user 对象，否则返回 None。因为 .objects.get() 方法没有查到或者多于一个，就会抛异常。

这里只用用户名与密码，先检测是否能够自定义成功。

```python
# 自定义 authenticate 实现邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户在 model 中是否存在，用 get 可以确保只有一个该用户
            user = UserProfile.objects.get(username=username)
            # 传入的密码，与 model 中的对比，只能使用 check_password 方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```





settings.py 中增加一个元组（第一个元素后面需要加逗号），帮刚才自定义的方法传进去：

```python
# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
```

调试可以进入。





