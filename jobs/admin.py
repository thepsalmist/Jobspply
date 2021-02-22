from django.contrib import admin
from .models import Job, Company, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "jobcategory", "expiry", "job_url", "status"]
    list_filter = ["status", "publish", "jobcategory"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    list_filter = [
        "title",
    ]
    prepopulated_fields = {"slug": ("title",)}
