from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Job


class JobSitemap(Sitemap):
    chagefreq = "weekly"
    priority = 0.9

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.updated


class StaticSitemap(Sitemap):
    def items(self):
        return [
            "career:home",
            "resume:home",
            "courses:home",
            "jobs:categories",
            "jobs:about",
            "jobs:contact",
        ]

    def location(self, item):
        return reverse(item)
