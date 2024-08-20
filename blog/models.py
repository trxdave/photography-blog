from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model representing a photo category (e.g., Landscape, Portrait).
    Each category has a unique name, description, slug, and associated image.
    """
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
        """
        Returns the display name of the category based on the name field.
        """
        return dict(self.CATEGORY_CHOICES).get(self.name, 'Unknown')


class Photo(models.Model):
    """
    Model representing a photo uploaded by a user. 
    Each photo has a title, content, description, category, image, associated user, and likes.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    categoryimage = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_photos'
    )
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='photo_likes', blank=True)

    def total_likes(self):
        """
        Returns the total number of likes for the photo.
        """
        return self.likes.count()

    def __str__(self):
        """
        Returns the title of the photo as its string representation.
        """
        return self.title


class Comment(models.Model):
    """
    Model representing a comment on a photo.
    Each comment is associated with a photo and a user, and includes text and a timestamp.
    """
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the comment showing the user and the photo it was made on.
        """
        return f"Comment by {self.user} on {self.photo}"