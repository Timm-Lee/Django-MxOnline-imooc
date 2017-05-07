# Django 顺序6_ModelForm



表单验证中设定的检验条件，有时和后面要存入的 model 非常类似，因此 Django 有方法把 model 转化成 form 用以表单验证，这种 form 名叫 ModelForm。



### 普通表单

```python
from django import forms

class UserAskForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=20)
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    course_name = forms.CharField(required=True, min_length=5, max_length=50)
```



经过对照 model（operation.UserAsk），发现字段的条件几乎相同。

唯一就是 form 中的 `require=True` 可以理解成 `null=False`。实际上字段也是默认不为空。

```python
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
```

所以 model 可以直接转化成 ModelForm 用。



### ModelForm

ModelForm 写成以下形式。其中 `model=UserAsk` 表示继承自 `UserAsk` 表，并且可以选择其中的字段，也可以像普通 form 一样，自己可以新增加字段。

```python
from operation.models import UserAsk

class AskUserForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
```



## urls 

首先在主 urls 下

```python
urlpatterns = [
    # 课程机构 url 配置
    url(r'^org/', include('organization.urls', namespace="org")),
]
```

在机构下面的 urls 中

```python
from .views import OrgView
urlpatterns = [
    # 课程机构列表页
    url(r'list/$', OrgView.as_view(), name="org_list"),
]
```









