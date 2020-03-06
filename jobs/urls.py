from django.urls import path
from . import views
from .views import home

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
    path("job/<slug:slug>/", views.job_detail, name="job_detail"),
    path("category/<str:query>/", views.jobs_by_category, name="jobs_by_category"),
]

