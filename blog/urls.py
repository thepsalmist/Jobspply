from django.urls import path
from . import views
from .views import post_list

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="blog"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("search/", views.search, name="search"),
]

