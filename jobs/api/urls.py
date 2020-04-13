from django.urls import path
from .views import JobsListAPIView, JobsDetailAPIView

app_name = "jobs_api"

urlpatterns = [
    path("", JobsListAPIView.as_view(), name="list"),
    path("<slug:slug>/", JobsDetailAPIView.as_view(), name="detail"),
]
