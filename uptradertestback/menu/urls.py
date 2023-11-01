from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu_view, name="home"),
    path('<str:item_url>/', views.menu_item_page, name='menu_item_page'),
]
