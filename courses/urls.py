from django.urls import path

from . import views
from .views import home

app_name = "courses"

urlpatterns = [
    path("", views.home, name="home"),
]
