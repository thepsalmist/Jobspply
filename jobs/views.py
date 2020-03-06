from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Job


def get_category_count():
    queryset = Job.objects.values("category").annotate(Count("category"))
    return queryset


def home(request):
    jobs = Job.objects.all()
    category_count = get_category_count()
    advertising = Job.objects.filter(category="Education")
    paginator = Paginator(jobs, 8)
    page = request.GET.get("page")
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        "jobs": jobs,
        "category_count": category_count,
        "page": page,
        "advertising": advertising,
    }
    return render(request, "jobs/index.html", context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    context = {"job": job}
    return render(request, "jobs/job_detail.html", context)


def jobs_by_category(request, query=None):
    jobs = Job.objects.all()
    if query is not None:
        lookup = Q(category__icontains=query)
        queryset = jobs.filter(lookup).all()

    context = {
        "jobs": jobs,
        "queryset": queryset,
    }
    return render(request, "jobs/category.html", context)
