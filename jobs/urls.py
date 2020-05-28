from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.job_search, name="job_search"),
    path("categories/", views.all_categories, name="categories"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
    path("job/<slug:slug>/", views.job_detail, name="job_detail"),
    path("category/<query>/", views.jobs_by_category, name="jobs_by_category"),
]
