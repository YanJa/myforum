from django.contrib import admin
from .models import Block
from article.models import Article
# Register your models here.


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name", "status")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "block", "content", "author", "status")

admin.site.register(Block, BlockAdmin)
admin.site.register(Article, ArticleAdmin)
