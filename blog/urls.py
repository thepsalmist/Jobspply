from django.urls import path
from . import views
from .views import post_list

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="blog"),
]

