from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Job
from career.models import Post


class JobSitemap(Sitemap):
    chagefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Job.objects.filter(status="published")

    def lastmod(self, obj):
        return obj.publish

    def location(self, obj):
        return obj.get_absolute_url()


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return [
            "career:home",
            "resume:home",
            "courses:home",
            "jobs:categories",
            "jobs:companies",
            "jobs:about",
            "jobs:contact",
        ]

    def location(self, item):
        return reverse(item)
