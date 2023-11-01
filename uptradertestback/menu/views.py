from django.shortcuts import render, get_object_or_404

from .models import MenuItem


def menu_view(request):
    menu = MenuItem.objects.get(name='main')  # Замените на нужное имя меню
    return render(request, 'index.html', {'menu': menu})


def menu_item_page(request, item_url):
    menu_item = get_object_or_404(MenuItem, url=item_url)
    return render(request, 'menu_item_page.html', {'menu_item': menu_item})
