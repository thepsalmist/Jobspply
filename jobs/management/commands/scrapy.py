from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import csv

from warehouse.models import Corporate


class Command(BaseCommand):
    help = " Scrapes CorporateSS Website"

    def handle(self, *args, **kwargs):

        source = requests.get("https://www.corporatestaffing.co.ke/jobs/").text

        soup = BeautifulSoup(source, "lxml")

        csv_file = open("jobs_kenya.csv", "w")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["title", "description", "link", "job_detail"])

        for article in soup.find_all("article"):

            try:
                title = article.find("header", class_="entry-header").text
                link = article.find("a", class_="entry-title-link")["href"]
                body = article.find("div", class_="entry-content")
                description = body.find("p").text

                if link is not None:
                    source = requests.get(link).text
                    soup = BeautifulSoup(source, "lxml")
                    job_detail = soup.find("div", class_="entry-content").text

            except Exception as e:
                title = None
                link = None
                body = None
                description = None

            if title and link and description is not None:
                try:
                    job = Corporate.objects.get(title=title, job_url=link)
                    print(f"{title} already exists")
                except Exception as e:
                    job = Corporate()
                    job.title = title
                    job.description = description
                    job.job_url = link
                    job.save()
                    print(f"{title} added")

            csv_writer.writerow([title, description, link, job_detail])

        csv_file.close

        self.stdout.write("job complete")
