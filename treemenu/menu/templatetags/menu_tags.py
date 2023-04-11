import re
from ..models import MenuListItem
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, name, parent=0):
    menu_items = MenuListItem.objects.filter(menu__name=name).select_related('parent')
    if parent != 0 and 'menu' in context:
        menu_items_data = context['menu']
    else:
        current_path = context['request'].path
        menu_items_data = []
        check_path = re.compile(r'^http[s]?://')
        for menu_item in menu_items:
            path = menu_item.path
            parent_id = menu_item.parent.id if menu_item.parent else 0
            is_active = True if path == current_path else False

            if check_path.match(path):
                is_url = True
                url = path
            else:
                is_url = False
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            menu_items_data.append({
                'id': menu_item.pk,
                'is_active': is_active,
                'parent': parent_id,
                'menu_item_name': menu_item.name,
                'name': name,
                'is_url': is_url,
                'url': url,
            })

    return {'menu': menu_items_data,
            'menu_items': (menu_item for menu_item in menu_items_data if menu_item['parent'] == parent)}
