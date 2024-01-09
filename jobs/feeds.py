from django.contrib.syndication.views import Feed
from .models import Job


class LatestJobsFeed(Feed):
    title = "Latest Jobs in Kenya 2024 | Jobsearchke"
    link = "/job/"
    description = "Jobs in Kenya 2024 - find the current job vacancies in Kenya 2024. Latest UN jobs kenya, ngo jobs kenya, government jobs kenya and part time jobs in kenya"

    def items(self):
        return Job.objects.all()[:50]

    def item_title(self, item):
        return item.get_job_title()

    def item_description(self, item):
        return item.description

    def item_lastupdated(self, item):
        return item.updated