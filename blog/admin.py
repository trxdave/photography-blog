from django.contrib import admin
from .models import Photo, Category


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'description',
        'image',
        'categoryimage')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
