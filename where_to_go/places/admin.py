from django.contrib import admin
from places.models import Image, Place
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    readonly_fields = ["place_preview"]
    fields = ('img', 'order_num', 'place_preview')

    def place_preview(self, obj):
        return format_html(f"<img src='{obj.img.url}' max-height='200' width='200' />")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
