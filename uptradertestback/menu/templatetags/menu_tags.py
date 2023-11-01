from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
    except MenuItem.DoesNotExist:
        return ""

    def build_menu_tree(parent):
        menu_items = MenuItem.objects.filter(parent=parent)
        menu_structure = []
        for item in menu_items:
            item_dict = {
                'name': item.name,
                'url': item.url,
                'children': build_menu_tree(item),
            }
            menu_structure.append(item_dict)
        return menu_structure

    menu_structure = build_menu_tree(menu)
    return menu_structure
