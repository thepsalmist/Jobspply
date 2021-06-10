import requests
import csv
from django.core.management.base import BaseCommand
from warehouse.models import Myjobmag
from bs4 import BeautifulSoup
from . import twitter, telegram, telethon


class Command(BaseCommand):
    help = "Scrapes MyJobMag "

    def handle(self, *args, **kwargs):
       	twitter.post_tweets()
	
        # base_url = "https://www.myjobmag.co.ke/"

        # csv_file = open("kenya_jobs.csv", "w")
        # csv_writer = csv.writer(csv_file)
        # csv_writer.writerow(
        #     [
        #         "job_title",
        #         "job_category",
        #         "job_date",
        #         "job_description",
        #         "job_link",
        #         "job_detail",
        #     ]
        # )

        # pages = [1, 2]

        # for i in pages:
        #     if i == 1:
        #         source = requests.get(base_url).text

        #     source = requests.get(base_url + "page/" + str(i)).text

        #     soup = BeautifulSoup(source, "lxml")

        #     for job_list in soup.find_all("li", class_="job-list-li"):

        #         try:

        #             job_title = job_list.find("li", class_="mag-b").text
        #             job_description = job_list.find("li", class_="job-desc").text
        #             job_link = job_list.find("li", class_="mag-b").a["href"]
        #             job_category = job_list.find("li", class_="job-item").a.text
        #             job_category = job_category.split("/")[0]
        #             job_date = job_list.find("li", id="job-date").text
        #             job_link = base_url + job_link
        #             job_thumbnail = str(
        #                 job_list.find("li", class_="job-logo").img["src"]
        #             )
        #             job_thumbnail = "%20".join(job_thumbnail.split())
        #             job_thumbnail = base_url + job_thumbnail

        #             if job_link is not None:
        #                 source = requests.get(job_link).text
        #                 soup = BeautifulSoup(source, "lxml")
        #                 job_detail = soup.find("li", class_="job-description").text

        #         except Exception as e:
        #             job_title = None
        #             job_thumbnail = None
        #             job_description = None
        #             job_link = None
        #             job_category = None
        #             job_detail = None
        #             job_date = None
        #             apply = None

        #         print(job_title)

        #         csv_writer.writerow(
        #             [
        #                 job_title,
        #                 job_category,
        #                 job_date,
        #                 job_description,
        #                 job_link,
        #                 job_detail,
        #             ]
        #         )

        #         if job_title and job_description and job_link is not None:
        #             # save to db
        #             try:
        #                 job = Myjobmag.objects.get(title=job_title, job_url=job_link)
        #                 print("%s already exists" % (job_title,))
        #             except Exception as e:
        #                 job = Myjobmag()
        #                 job.title = job_title
        #                 job.description = job_description
        #                 job.job_url = job_link
        #                 job.category = job_category
        #                 job.thumbnail = job_thumbnail
        #                 job.body = job_detail

        #                 job.save()
        #                 print("%s added" % (job_title,))

        # csv_file.close()

        self.stdout.write("job complete")
