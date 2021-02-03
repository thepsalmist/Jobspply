from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "category", "job_url", "slug", "status"]
    list_filter = ["status", "publish", "category"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]
