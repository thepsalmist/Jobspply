from django.urls import path
from . import views

app_name = "marketing"

urlpatterns = [
    path("", views.email_list_signup, name="subscribe"),
]

