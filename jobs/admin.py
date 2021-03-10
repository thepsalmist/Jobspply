from django.contrib import admin
from .models import Job, Company, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "company",
        "jobcategory",
        "publish",
        "expiry",
        "job_url",
        "status",
    ]
    list_filter = ["status", "company", "jobcategory", "publish"]
    search_fields = ["title", "description"]
    ordering = ["-publish"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_filter = [
        "name",
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    list_filter = [
        "title",
    ]
    prepopulated_fields = {"slug": ("title",)}
