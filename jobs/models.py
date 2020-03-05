from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    job_url = models.URLField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return self.title

