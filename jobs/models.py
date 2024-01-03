from datetime import timedelta
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
        ("project_management", "Project Management"),
        ("general", "General"),
        ("travels & tours", "Travels & Tours"),
        ("product management", "Product Management"),
        ("driving","Driving"),

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
        ("archived", "Archived"),
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
    description = models.TextField(null=True, blank=True)
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
    expiry = models.DateField(null=True, blank=True)
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

    def save(self, *args, **kwargs):
        self.expiry = self.set_expiry_date()
        self.description = self.set_description()
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("jobs:job_detail", args=[self.slug])

    def get_job_title(self):
        res = f"{self.title} - {self.company.name}"
        return res

    def get_job_url(self):
        job_url = "https://jobsearchke.com/job/" + self.slug
        return job_url

    def set_expiry_date(self):
        published_date = self.publish.date()
        one_month = timedelta(days=30)
        return published_date + one_month
    
    def set_description(self):
        description = f"{self.company.name} careers, {self.company.name} salaries. 2024 Job vacancies at {self.company.name} for {self.title} in Kenya. Apply today."
        return description

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
        instance.slug = slug_generator(
            instance, instance.get_job_title(), instance.slug
        )


pre_save.connect(slug_save, sender=Job)
