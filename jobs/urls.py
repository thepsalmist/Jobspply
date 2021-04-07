from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views
from .feeds import LatestJobsFeed

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.job_search, name="job_search"),
    path("categories/", views.all_categories, name="categories"),
    path("companies/", views.all_companies, name="companies"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
    path("job/<slug:slug>/", views.job_detail, name="job_detail"),
    path("jobs-at/<slug:slug>/", views.jobs_by_company, name="jobs_by_company"),
    path("category/<slug:slug>/", views.jobs_by_category, name="jobs_by_category"),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt"))),
    path("feed/", LatestJobsFeed(), name="job_feed"),
]
