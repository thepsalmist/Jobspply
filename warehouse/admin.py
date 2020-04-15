from django.contrib import admin
from .models import Myjobmag, Corporate, Jobskenya


@admin.register(Myjobmag)
class MyjobmagAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "category", "job_url", "slug"]
    list_filter = ["publish", "category"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]


@admin.register(Corporate)
class CorporateAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "job_url", "slug"]
    list_filter = ["publish"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]


@admin.register(Jobskenya)
class JobskenyaAdmin(admin.ModelAdmin):
    list_display = ["title", "date_posted", "publish", "job_url", "slug"]
    list_filter = ["publish"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]
