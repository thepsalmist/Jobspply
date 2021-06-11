import telebot
import pytz
import time
from django.core.management.base import BaseCommand
from decouple import config
from datetime import datetime
from datetime import timedelta
from jobs.models import Job


class Command(BaseCommand):
    help = "Post Job updates to Telegram"

    def handle(self, *args, **kwargs):

        access_token = config("telegram_access_token")

        bot = telebot.TeleBot(
            access_token, parse_mode=None
        )  # You can set parse_mode by default. HTML or MARKDOWN

        now = datetime.now(tz=pytz.UTC)
        one_hour_ago = now - timedelta(hours=3)
        jobs = Job.objects.filter(publish__gte=one_hour_ago)

        for job in jobs:
            job_title = job.get_job_title()
            job_description = job.description
            job_slug = job.slug
            job_url = "https://jobsearchke.com/job/" + job_slug

            job = job_title + " " + str(job_url)

            bot.send_message(chat_id="@jobsearchke", text=job)

            time.sleep(60)

        self.stdout.write("job complete")
