from django.db import models
from django.db.models.signals import pre_save
from jobspply.utils import slug_generator


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance, instance.title, instance.slug)


class Myjobmag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    job_url = models.URLField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title


pre_save.connect(slug_save, sender=Myjobmag)


class Corporate(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    job_url = models.URLField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title


pre_save.connect(slug_save, sender=Corporate)


class Jobskenya(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    date_posted = models.CharField(max_length=50)
    job_url = models.URLField()
    description = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title


pre_save.connect(slug_save, sender=Jobskenya)
