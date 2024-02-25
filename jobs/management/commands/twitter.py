from datetime import datetime
from datetime import timedelta
import pytz
import time
import tweepy
from decouple import config
from jobs.models import Job


def twitter_auth():
    # Get twitter Auth credentials
    consumer_key = config("TWITTER_API_KEY")
    consumer_secret = config("TWITTER_API_KEY_SECRET")
    access_token_secret = config("TWITTTER_ACCESS_TOKEN_SECRET")
    access_token = config("TWITTER_ACCESS_TOKEN")

    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    
    return client

def post_tweets():
    client = twitter_auth()
    if not client:
        raise Exception("Twitter Authentication failed")
    
    now = datetime.now(tz=pytz.UTC)
    three_hours_ago = now - timedelta(hours=3)
    jobs = Job.objects.filter(publish__gte=three_hours_ago)
    for job in jobs:
        job_title = job.get_job_title()
        job_description = job.description
        job_slug = job.slug
        job_url = f"https://jobsearchke.com/job/{job_slug}"
        
        tweet_content = f"#IkoKaziKE Check out this job opportunity:\n {job_title}\n{job_url}\n{job_description}"
        client.create_tweet(
            text=tweet_content
        )
        time.sleep(60)



# def get_trending():
#     # Constrct the API instance
#     api = tweepy.API(twitter_auth())

#     # WOEID of Kenya
#     woeid = 23424863

#     # fetch trends
#     trends = api.trends_place(id=woeid)
#     top_trends = []
#     # print(trends)
#     # print("The top trends in Kenya are:")

#     for value in trends:
#         for trend in value["trends"]:
#             top_trends.append(trend["name"])
#         mylist = top_trends[:5]

#     return mylist