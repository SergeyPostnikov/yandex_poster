from django.contrib import admin
from places.models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
