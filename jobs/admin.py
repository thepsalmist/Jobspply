from django.contrib import admin
from .models import Job, Company, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "category", "job_url", "slug", "status"]
    list_filter = ["status", "publish", "category"]
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
