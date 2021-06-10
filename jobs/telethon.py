import pytz
import time
import asyncio
from telethon import TelegramClient, events, sync
from asgiref.sync import sync_to_async
from decouple import config
from datetime import datetime
from datetime import timedelta
from .models import Job


# Creating a client
api_id = config("api_id")
api_hash = config("api_hash")

client = TelegramClient("server", api_id, api_hash)

now = datetime.now(tz=pytz.UTC)
two_hours_ago = now - timedelta(hours=2)

new_jobs = []


@sync_to_async
def get_jobs():
    jobs = Job.objects.filter(publish__gte=two_hours_ago)
    # jobs = Job.objects.all()
    for job in jobs:
        data = {
            "job_title": job.get_job_title(),
            "job_description": job.description,
            "job_slug": job.slug,
            "job_url": job.get_job_url(),
        }
        new_jobs.append(data)
    return new_jobs


async def main():
    jobs = await get_jobs()
    for job in jobs:
        new_job = job["job_title"] + " " + str(job["job_url"])

        # for job in await get_jobs():
        #     job_title = job.get_job_title()
        #     job_description = job.description
        #     job_slug = job.slug
        #     job_url = "https://jobsearchke.com/job/" + job_slug

        #     job = job_title + " " + str(job_url)

        # You can send messages to yourself...
        # await client.send_message('me', job)

        # ...to some chat ID
        # await client.send_message(-1001294903048, new_job)
        await client.send_message(-1001319879826, new_job)

        time.sleep(60)
