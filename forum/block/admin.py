from django.contrib import admin
from .models import Block
# Register your models here.


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name")

admin.site.register(Block, BlockAdmin)
