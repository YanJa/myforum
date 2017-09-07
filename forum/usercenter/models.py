from django.db import models
from datetime import datetime
# Create your models here.


# 存储用于激活用户的信息
class UserProfile(models.Model):
    username = models.CharField("用户", max_length=150)
    active_code = models.CharField("激活码", max_length=150)
    overdue_time = models.DateTimeField("过期时间")

