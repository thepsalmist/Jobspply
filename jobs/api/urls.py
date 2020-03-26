from django.urls import path
from .views import JobsListAPIView

app_name = "jobs_api"

urlpatterns = [
    path("", JobsListAPIView.as_view(), name="list"),
]
