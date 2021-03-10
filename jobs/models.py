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
    slug = models.SlugField(max_length=256, null=True)
    description = models.TextField()
    logo = models.ImageField(default="logo.png", upload_to="Company/Logos")
    apply = HTMLField(blank=True, null=True)
    # published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "company"
        verbose_name_plural = "companies"


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("sales & marketing", "Sales/Marketting"),
        ("accounting & finance", "Accounting/Finance"),
        ("software engineering", "Software/Engineering"),
        ("ict & telecommunications", "ICT/Telecommunications"),
        ("manufacturing & production", "Manufacturing/Production"),
        ("ngo", "NGO"),
        ("education & teaching", "Education/Teaching"),
        ("media & social_media", "Media/Social_Media"),
        ("healthcare & medical", "Healthcare/Medical"),
        ("banking & insurance", "Banking/Insurance"),
        ("logistics & procurement", "Logistics/Procurement"),
        ("internship", "Internship"),
        ("hotels & hospitality", "Hotels/Hospitality"),
        ("government & parastatals", "Government/Parastatals"),
        ("management", "Management"),
        ("data science", "Data Science"),
        ("hr & admin assistant", "HR/Admin Assistant"),
        ("customer service", "Customer Service"),
        ("engineering", "Engineering"),
    )
    title = models.CharField(choices=CATEGORY_CHOICES, max_length=256)
    slug = models.SlugField(max_length=256, blank=True)
    icon = models.CharField(max_length=50)

    class Meta:
        ordering = ("title",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:jobs_by_category", args=[self.slug])


class Job(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    jobcategory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    location = models.CharField(
        max_length=100, choices=LOCATION_CHOICES, default="nairobi", null=True
    )
    salary = models.CharField(max_length=50, default="confidential", null=True)
    employment_type = models.CharField(
        max_length=50, choices=EMPLOYMENT_CHOICES, default="fulltime", null=True
    )
    job_url = models.URLField(default=SITE_URL)
    # thumbnail = models.URLField(blank=True, null=True)
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
    # apply = HTMLField(blank=True, null=True)
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
