from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    categories = models.CharField(max_length=100)
    job_url = models.URLField()
    thumbnail = models.URLField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return self.title

