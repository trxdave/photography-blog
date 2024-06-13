from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    def __str__(self):
        return self.name

"""Model for Blog posts"""

class Photo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=50,null=True,blank=False,)
    description = models.CharField(max_length=500,null=True,blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True,auto_created=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


"""Model for user comments"""

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.CharField(max_length=100,null=True,blank=False)
    message = models.TextField(max_length=200,null=True,blank=False)
    created = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.message

