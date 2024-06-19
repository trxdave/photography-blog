from django.contrib import admin
from.models import Photo

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

admin.site.register(Photo, PostAdmin)