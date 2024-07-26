from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'description', 'image', 'category')

    def description(self, obj):
        return obj.description

admin.site.register(Photo, PhotoAdmin)