import pytz
import time
import random
import asyncio
from telethon import TelegramClient, events, sync
from asgiref.sync import sync_to_async
from decouple import config
from datetime import datetime
from datetime import timedelta
from decouple import config
from .models import Job


# Creating a client
api_id = config("api_id")
api_hash = config("api_hash")

#Telegram IDs
amx_id = config("amx_id")
rolodex_id = config("rolodex_id")
eng_id = config("engineering_id")
coding_id = config("coding_id")

client = TelegramClient("server", api_id, api_hash)

now = datetime.now(tz=pytz.UTC)
two_hours_ago = now - timedelta(hours=2)

new_jobs = []
dev_jobs = []
eng_jobs = []

time_list = [60, 120, 180]


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
        if job.jobcategory.title == "software engineering":
            dev_jobs.append(data)
        elif job.jobcategory.title == "engineering":
            eng_jobs.append(data)
        else:
            new_jobs.append(data)

    return new_jobs,dev_jobs,eng_jobs


async def main():
    new_jobs, dev_jobs,eng_jobs = await get_jobs()
    for job in new_jobs:
        new_job = job["job_title"] + " " + str(job["job_url"])

        # You can send messages to yourself...
        # await client.send_message('me', job)

        # ...to some chat ID
        #amx_community
        await client.send_message(amx_id, new_job)
        
        #rolodex
        await client.send_message(rolodex_id, new_job)
       
        time.sleep(random.choice(time_list))

    for job in dev_jobs:
        new_job = job["job_title"] + " " + str(job["job_url"])
        await client.send_message(coding_id, new_job)

        time.sleep(random.choice(time_list))
    
    for job in eng_jobs:
        new_job = job["job_title"] + " " + str(job["job_url"])
        await client.send_message(eng_id, new_job)

        time.sleep(random.choice(time_list))
