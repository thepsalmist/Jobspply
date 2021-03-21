from datetime import datetime
from datetime import timedelta
import pytz
import time
import tweepy
from decouple import config
from jobs.models import Job


def twitter_auth():
    # Get twitter Auth credentials
    consumer_key = config("api_key")
    consumer_secret = config("api_key_secret")
    access_token = config("access_token")
    access_token_secret = config("access_token_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth


def get_trending():
    # Constrct the API instance
    api = tweepy.API(twitter_auth())

    # WOEID of Kenya
    woeid = 23424863

    # fetch trends
    trends = api.trends_place(id=woeid)
    top_trends = []
    # print(trends)
    # print("The top trends in Kenya are:")

    for value in trends:
        for trend in value["trends"]:
            top_trends.append(trend["name"])
        mylist = top_trends[:5]

    return mylist


def post_tweets():
    api = tweepy.API(twitter_auth())
    mylist = get_trending()

    now = datetime.now(tz=pytz.UTC)
    one_hour_ago = now - timedelta(hours=3)
    jobs = Job.objects.filter(publish__gte=one_hour_ago)
    for job in jobs:
        job_title = job.get_job_title()
        job_description = job.description
        job_slug = job.slug
        job_url = "https://jobsearchke.com/job/" + job_slug

        job = job_title + " " + str(job_url)

        api.update_status(
            status="#IkoKaziKE Check out this job opportunity \n {} {} {} {} {} {}".format(
                job, mylist[0], mylist[1], mylist[2], mylist[3], mylist[4]
            )
        )
        time.sleep(60)
