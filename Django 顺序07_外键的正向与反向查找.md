# Django 顺序7_外键的正向与反向查找



## 正向查找到对应的外键 外键_id

获取到外键的id。其中 city 是外键，通过 `外键_id` 获得外键，这里是 `city_id`。

organisation.views.py

```python
class OrgView(View):
    def get(self, request):
        # 城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
```

在模板中可以取外键，然后直接去外键的名称

```python
<span class="fl">{{ course.course_org.name }}</span>
```

其中 course 是 model 名称，course_org 是该 model 中的字段名，name 是外键中的字段名。





## 通过外键，查找关联该外键的数据 外键.查询表_set

organisation.views.py

```python
class OrgHomeVie(View):
    """
    机构详情首页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # couse 的外键指向了 org，如果想（反向的）了解 org 下面有多少 course
        # jango 提供的方法 course_set 即 <modelName>_set
        all_courses = course_org.course_set.all()
        all_teachers = course_org.teacher_set.all()
```

