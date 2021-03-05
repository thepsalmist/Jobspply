from django.contrib.syndication.views import Feed
from .models import Job


class LatestJobsFeed(Feed):
    title = "Latest Jobs in Kenya 2021 | Jobsearchke"
    link = "/job/"
    description = "Jobs in Kenya 2021 - JobsearchKE provides the latest job vaccancies in Kenya 2021. Signup and get updates on ngo jobs, government jobs and part time jobs in Kenya. Visit our career page and courses to enhance your career"

    def items(self):
        return Job.objects.all()[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
