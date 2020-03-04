from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, unique_for_date="publish")
    description = models.TextField()
    job_url = models.URLField()
    thumbnail = models.ImageField(default="jobs.png", upload_to="Jobs %Y%M%d")
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

