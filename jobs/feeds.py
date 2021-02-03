from django.contrib.syndication.views import Feed
from .models import Job


class LatestJobsFeed(Feed):
    title = "Jobsearchke Latest Jobs"
    link = "/job/"
    description = "Latest Job Opportunities in Kenya"

    def items(self):
        return Job.published.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
