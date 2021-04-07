from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class BlogSitemap(Sitemap):
    chagefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.publish
