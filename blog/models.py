from django.db import models
from cloudinary.models import CloudinaryField

CATEGORY_CHOICES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('wildlife', 'Wildlife'),
        ('street', 'Street'),
        ('macro', 'Macro'),
]

class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)

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