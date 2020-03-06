from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Job


def get_jobs_by_category():
    queryset = Job.objects.order_by("category")
    for query in queryset:
        query = query.category
    return query


def get_category_count():
    queryset = Job.objects.values("category").annotate(Count("category"))
    return queryset


def home(request):
    jobs = Job.objects.all()
    categories = Job.objects.filter(category="Banking").all()
    category_count = get_category_count()
    context = {
        "jobs": jobs,
        "category_count": category_count,
        "categories": categories,
    }
    return render(request, "jobs/index.html", context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    context = {"job": job}
    return render(request, "jobs/job_detail.html", context)
