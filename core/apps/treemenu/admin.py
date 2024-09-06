from django.contrib import admin

from core.apps.treemenu.models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "menu")
    search_fields = ("title",)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
