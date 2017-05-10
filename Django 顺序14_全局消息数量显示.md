# Django 顺序14_全局消息数量显示

## 顺序

* request.user 在模板中是全局存在的
* 在 request.user 定义获取未读消息数量的方法
* 模板中调用获取数量的方法



## Model 中设置方法

在 users/models.py 中 UserProfile 中定义获取未读消息数量的方法

首先，在方法中引入 `operation.models` ，如果在开头就引入会形成循环引用。

然后，把用户 id 传入 UserMessage 中（因为 UserMessage 不是用外键，而是用 id ），返回 `count()` 数量即可。

```python
class UserProfile(AbstractUser):
    #...
    def unread_nums(self):
        # 获取用户未读消息数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id).count()
```



## html 中显示数量

直接调用`{{ request.user.unread_nums }}`

```html
<div class="msg-num">
  <span id="MsgNum">{{ request.user.unread_nums }}</span>
</div>
```























