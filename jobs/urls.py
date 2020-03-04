from django.urls import path
from . import views
from .views import home

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
]

