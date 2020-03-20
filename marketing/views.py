from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from .models import SignUp

import requests
import json

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0"
members_endpoint = f"{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members"


def subscribe(email):
    # create object/data that we post
    data = {"email_address": email, "status": "subscribed"}
    r = requests.post(
        members_endpoint, auth=("", MAILCHIMP_API_KEY), data=json.dumps(data)
    )

    return r.status_code, r.json


def email_list_signup(request):
    # Newsletter Signup
    if request.method == "POST":
        s_form = SignUpForm(request.POST)
        if s_form.is_valid():
            email_qs = SignUp.objects.filter(email=s_form.instance.email)
            if email_qs.exists():
                messages.success(request, "Thanks!,you already subscribed!")
            else:
                subscribe(s_form.instance.email)
                s_form.save()
                messages.success(request, "Thank you for subscribing to our newsletter")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        s_form = SignUpForm()
