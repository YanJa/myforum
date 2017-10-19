from django.db import models

# Create your models here.
class Block(models.Model):
    """
    版块模型,存放版块数据
    """
    name = models.CharField("版块名称", max_length=100)
    manger = models.CharField("管理员", max_length=50)
    desc = models.TextField("版块描述", max_length=200)
