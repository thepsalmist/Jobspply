import datetime
from datetime.date import today
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
    tdy = today.strftime("%y-%m-%d")
    jobs = Job.objects.all()
    for job in jobs:
        published = job.publish.today().strftime("%y-%m-%d")

    api = tweepy.API(twitter_auth())
    mylist = get_trending()
    job = (
        "Lab Technician Job Kenya (50-65K) - Dairy Company"
        + " https://jobsearchke.com/job/lab-technician-job-kenya-50-65k-dairy-company/ "
    )
    api.update_status(
        status="#IkoKaziKE Check out this job opportunity \n {} {} {} {} {} {}".format(
            job, mylist[0], mylist[1], mylist[2], mylist[3], mylist[4]
        )
    )


# publish__gte=2021-01-23+00%3A00%3A00%2B00%3A00&publish__lt=2021-01-24+00%3A00%3A00%2B00%3A00

# publish__gte=2021-01-25+00%3A00%3A00%2B00%3A00&publish__lt=2021-01-26+00%3A00%3A00%2B00%3A00