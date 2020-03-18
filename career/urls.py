from django.urls import path
from . import views
from .views import post_list

app_name = "career"

urlpatterns = [
    path("", views.post_list, name="home"),
    path("category/<slug:category_slug>/", views.post_list, name="post_category"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("search/", views.search, name="search"),
]
