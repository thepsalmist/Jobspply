from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce import HTMLField
from django.db.models.signals import pre_save
from jobspply.utils import slug_generator


class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    body = HTMLField()
    category = models.CharField(max_length=100)
    job_url = models.URLField()
    thumbnail = models.URLField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job_detail", args=[self.slug])


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Job)
