from django.contrib import admin
from .models import MenuListItem, Menu
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(MenuListItem)
class MenuListItemAdmin(admin.ModelAdmin):
    fields = ['name','menu', 'parent']
