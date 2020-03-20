from django.db import models
from tinymce import HTMLField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("interviews", "INTERVIEWS"),
        ("career_development", "CAREER_DEVELOPMENT"),
        ("resumes", "RESUMES"),
        ("salaries", "SALARIES"),
    )
    title = models.CharField(
        choices=CATEGORY_CHOICES, max_length=100, default="interviews"
    )
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("career:post_category", args=[self.slug])


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="Author.jpg", upload_to="Authors")

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, unique_for_date="publish")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts", default=1
    )
    body = HTMLField()
    image = models.ImageField(default="post.jpeg", upload_to="Post %Y%M%d")
    publish = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "career:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
