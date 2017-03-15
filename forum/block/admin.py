from django.contrib import admin
from .models import Block
from article.models import Article
# Register your models here.


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name", "status")

admin.site.register(Block, BlockAdmin)
admin.site.register(Article)
