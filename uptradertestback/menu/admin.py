from django.contrib import admin

from .models import MenuItem


# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')


admin.site.register(MenuItem, MenuItemAdmin)
