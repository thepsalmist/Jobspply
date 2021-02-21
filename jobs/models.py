from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce import HTMLField
from django.db.models.signals import pre_save
from jobspply.utils import slug_generator

SITE_URL = "https://jobsearchke.com/"


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(default="logo.png", upload_to="Company/Logos")

    def __str__(self):
        return self.name


class Job(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("pulished", "Published"),
    )
    EMPLOYMENT_CHOICES = (
        ("contract", "Contract"),
        ("fulltime", "Fulltime"),
        ("remote", "Remote"),
    )
    LOCATION_CHOICES = (
        ("nairobi", "Nairobi"),
        ("mombasa", "Mombasa"),
        ("kisumu", "Kisumu"),
        ("nakuru", "Nakuru"),
        ("eldoret", "Eldoret"),
        ("kakamega", "Kakamega"),
    )
    company = models.ForeignKey(Company, null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(
        max_length=100, choices=LOCATION_CHOICES, default="nairobi", null=True
    )
    salary = models.CharField(
        help="30K", max_length=50, default="confidential", null=True
    )
    employment_type = models.CharField(
        max_length=50, choices=EMPLOYMENT_CHOICES, default="fulltime", null=True
    )
    job_url = models.URLField()
    thumbnail = models.URLField(blank=True, null=True)
    # image = models.ImageField(
    #     default="logo.png", blank=True, null=True, upload_to="Logos %Y%M%d"
    # )
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    expiry = models.DateField(null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft", null=True
    )
    body = HTMLField()
    apply = HTMLField(blank=True, null=True)
    # published = PublishedManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job_detail", args=[self.slug])

    @property
    def structured_data(self):
        url = SITE_URL + self.get_absolute_url()
        data = {
            "@type": "JobPosting",
            "title": self.title,
            "description": self.description,
            "datePosted": self.publish.strftime("%Y-%m-%d"),
            "validThrough": self.expiry.strftime("%Y-%m-%d"),
            "employmentType": self.employment_type,
            "hiringOrganization": self.company,
            "jobLocation": self.location,
            "baseSalary": self.salary,
        }

        return data


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Job)
