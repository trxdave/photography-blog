from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, help_text='Enter the category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name