from ..models import Menu, MenuListItem
from django import template

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu():
    menus = Menu.objects.all()
    return {'menu':menus}