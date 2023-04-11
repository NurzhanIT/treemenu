from django.contrib import admin
from .models import MenuListItem, Menu
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(MenuListItem)
class MenuListItemAdmin(admin.ModelAdmin):
    fields = ['name','menu', 'parent', 'path']

    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['path'].widget.attrs['placeholder'] = '/example/example/example'
        return super().render_change_form(request, context, *args, **kwargs)
