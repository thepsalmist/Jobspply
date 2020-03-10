from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.job_search, name="job_search"),
    path("job/<slug:slug>/", views.job_detail, name="job_detail"),
    path("category/<query>/", views.jobs_by_category, name="jobs_by_category"),
]

