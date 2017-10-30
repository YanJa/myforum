from django.db import models

# Create your models here.
class Block(models.Model):
    """
    版块模型,存放版块数据
    """
    name = models.CharField("版块名称", max_length=100)
    manger = models.CharField("管理员", max_length=50)
    desc = models.TextField("版块描述", max_length=200)
    status = models.IntegerField("状态", choices=((0, "正常"), (-1, "删除")))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "版块"
        # verbose_name_plural 是版块的复数
        verbose_name_plural = "版块"
