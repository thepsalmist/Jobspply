from django.db import models
from tinymce import HTMLField
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.jpeg", upload_to="Authors")

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, unique_for_date="publish")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    body = HTMLField()
    image = models.ImageField(default="post.jpeg", upload_to="Post %Y%M%d")
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
