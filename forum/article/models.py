from django.db import models
from block.models import Block
# Create your models here.


class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name="所属版块")  # block外键,这个列是别个表的主键
    title = models.CharField("文章名称", max_length=100)
    content = models.CharField("文章描述", max_length=1000)
    author = models.CharField("文章作者", max_length=20)
    status = models.IntegerField("状态", choices=((0, "正常"), (1, "删除")))
    create_timestamp = models.DateTimeField("创建时间", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("最后更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        # 显示在admin后台首页的名字， plural为复数状态
        verbose_name = "文章"
        verbose_name_plural = "文章"
