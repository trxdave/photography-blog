from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

class MyModel(models.Model):
    image = CloudinaryField('image')

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, help_text='Enter the category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, help_text='Enter the post title')
    content = models.TextField(blank=False, help_text='Enter the post content')
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'category')

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=False, help_text='Enter the photo title')
    image = models.ImageField(upload_to='images/', blank=False, help_text='Select an image file')
    description = models.TextField(blank=True, help_text='Enter a description of the photo')
    slug = models.SlugField(unique=True)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title

class LandscapeImage(models.Model):
    image = models.ImageField(upload_to='landscape_images/', blank=False, help_text='Select an image file')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uploaded_at)