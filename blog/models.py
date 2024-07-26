from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, help_text='Enter the category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = CloudinaryField('image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title