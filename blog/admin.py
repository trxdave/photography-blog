from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'description', 'image')

admin.site.register(Photo, PhotoAdmin)