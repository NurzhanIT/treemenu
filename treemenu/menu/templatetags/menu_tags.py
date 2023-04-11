from ..models import Menu, MenuListItem
from django import template
from django.template import RequestContext
register = template.Library()


@register.inclusion_tag('menu.html',takes_context=True)
def draw_menu(context, name, parent=0):

    menu_items = MenuListItem.objects.filter(menu__name=name)
    if parent != 0 and 'menu' in context:
        print(context['menu'])
        menu_items_data = context['menu']
    elif parent == 0 and 'menu' not in context:
        current_path = context['request'].path
        menu_items_data=[]

        for menu_item in menu_items:

            parent_id = menu_item.parent.id if menu_item.parent else 0
            print(parent_id)
            print(menu_item.pk, 'id')
            is_active = True if menu_item.path == current_path and current_path else False

            menu_items_data.append({
                'id':  menu_item.pk,
                'path': menu_item.path,
                'current_path':current_path,
                'is_active': is_active,
                'parent': parent_id,
                'menu_item_name':menu_item.name,
                'name':name,
            })
            print(menu_items_data, 'menu_items_data')

    return {'menu': menu_items_data}
