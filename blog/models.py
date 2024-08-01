from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    categoryimage = models.CharField(max_length=225)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title