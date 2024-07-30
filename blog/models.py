from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):

    LANDSCAPE = 'Landscape'
    PORTRAIT = 'Portrait'
    WILDLIFE = 'Wildlife'
    STREET = 'Street'
    MACRO = 'Macro'

    CATEGORY_CHOICES = [
        (LANDSCAPE, 'Landscape'),
        (PORTRAIT, 'Portrait'),
        (WILDLIFE, 'Wildlife'),
        (STREET, 'Street'),
        (MACRO, 'Macro'),
    ]

    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title