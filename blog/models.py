from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title