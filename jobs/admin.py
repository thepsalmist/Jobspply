from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "job_url"]
    list_filter = ["publish"]
    search_fields = ["title", "description"]
    ordering = ["publish"]
