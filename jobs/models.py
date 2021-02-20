from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce import HTMLField
from django.db.models.signals import pre_save
from jobspply.utils import slug_generator


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Job(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("pulished", "Published"),
    )
    LOCATION_CHOICES = (
        ("nairobi", "Nairobi"),
        ("mombasa", "Mombasa"),
        ("kisumu", "Kisumu"),
        ("nakuru", "Nakuru"),
        ("eldoret", "Eldoret"),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    job_url = models.URLField()
    thumbnail = models.URLField(blank=True, null=True)
    image = models.ImageField(
        default="logo.png", blank=True, null=True, upload_to="Logos %Y%M%d"
    )
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    expiry = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    body = HTMLField()
    apply = HTMLField(blank=True, null=True)
    # published = PublishedManager()

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


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(default="logo.png", upload_to="Company/Logos")

    def __str__(self):
        return self.name
