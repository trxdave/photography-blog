from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'description', 'image', 'get_category')

    def get_category(self,obj):
        return obj.category.name

admin.site.register(Photo, PhotoAdmin)