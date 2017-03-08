from django.db import models

# Create your models here.


class Block(models.Model):
    name = models.CharField("板块名称", max_length=20)
    desc = models.CharField("板块描述", max_length=200)
    manager_name = models.CharField("管理员名称", max_length=20)
