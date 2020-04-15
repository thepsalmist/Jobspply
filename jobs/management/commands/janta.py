from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import requests
import csv

from warehouse.models import Jobskenya


class Command(BaseCommand):
    help = " Scrape Jobs in Kenya"

    def handle(self, *args, **kwargs):

        base_url = "https://www.jobsinkenya.co.ke/jobs-in-kenya/page/"

        source = []

        csv_file = open("janta.csv", "w")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["job_title", "date_posted", "job_description", "job_url"])
        pages = [1, 2]

        for i in pages:
            source = requests.get(base_url + str(i)).text
            soup = BeautifulSoup(source, "lxml")
            print(i)
            for article in soup.find_all("article"):
                print(base_url + str(i))
                try:
                    job_title = article.find("header", class_="entry-header").text
                    date_posted = article.find("a", class_="updated").text
                    job_url = article.find("a", class_="updated")["href"]

                    if job_url is not None:
                        source = requests.get(job_url).text
                        soup = BeautifulSoup(source, "lxml")
                        job_description = soup.find("div", class_="entry-content").text

                except Exception as e:
                    job_url = None
                    job_title = None
                    date_posted = None
                    job_description = None

                if job_title and job_url and job_description is not None:
                    try:
                        job = Jobskenya.objects.get(title=job_title, job_url=job_url)
                        print(f"{job_title} already exists")
                    except Exception as e:
                        job = Jobskenya()
                        job.title = job_title
                        job.job_url = job_url
                        job.date_posted = date_posted
                        job.description = job_description

                        job.save()
                        print(f"{job_title} added")

            csv_writer.writerow(
                [job_title, date_posted, job_description, job_url,]
            )
        csv_file.close()

        self.stdout.write("job complete")
