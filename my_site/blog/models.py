from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=100)
    date = models.TimeField()
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    caption = models.CharField(max_length=100)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.caption}"