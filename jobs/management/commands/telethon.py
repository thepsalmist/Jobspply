import pytz
import time
from telethon import TelegramClient,events, sync
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async
from decouple import config
from datetime import datetime
from datetime import timedelta


class Command(BaseCommand):
    help = "Post Job updates to Telegram"

    def handle(self, *args, **kwargs):
        # Creating a client
        api_id = config('api_id')
        api_hash = config('api_hash')

        client = TelegramClient('server',api_id,api_hash)
    
        @sync_to_async
        def get_jobs():
            jobs = Job.objects.filter(publish__gte=three_hours_ago)
            return jobs


        async def main():
            now = datetime.now(tz=pytz.UTC)
            three_hours_ago = now - timedelta(hours=3)
            

            for job in await get_jobs():
                job_title = job.get_job_title()
                job_description = job.description
                job_slug = job.slug
                job_url = "https://jobsearchke.com/job/" + job_slug


                job = job_title + " " + str(job_url)

                # You can send messages to yourself...
                #await client.send_message('me', job)

                # ...to some chat ID
                await client.send_message(-1001294903048, job)
                #await client.send_message(-1001294903048, job)

                time.sleep(60)
            
        with client:
            client.loop.run_until_complete(main())