from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Landscape'),
        (2, 'Portrait'),
        (3, 'Wildlife'),
        (4, 'Street'),
        (5, 'Macro'),
    )

    name = models.IntegerField(choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.name, 'Unknown')

class Photo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    categoryimage = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_photos')
    image = CloudinaryField('image')

    def __str__(self):
        return self.title