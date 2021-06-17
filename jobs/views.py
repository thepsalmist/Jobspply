import re
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from collections import Counter
from .models import Job, Company, Category
from career.models import Post
from marketing.models import SignUp
from marketing.forms import SignUpForm
from users.forms import ContactForm


# def get_category():
#     categories = []
#     jobs = Job.objects.all()
#     for job in jobs:
#         categories.append(job.category)
#         categories = list(set(categories))

#     return categories


def home(request):
    jobs = Job.objects.filter(status="published")
    latest_posts = Post.objects.order_by("-publish")[:3]
    categories = Category.objects.all()
    companies = Company.objects.all()
    paginator = Paginator(jobs, 15)
    page = request.GET.get("page")
    s_form = SignUpForm()

    # Newsletter Signup
    # if request.method == "POST":
    #     s_form = SignUpForm(request.POST)
    #     if s_form.is_valid():
    #         s_form.save()
    #         messages.success(request, "Thank you for subscribing to our newsletter")
    #         return redirect("jobs:home")
    # else:
    #     s_form = SignUpForm()

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        "jobs": jobs,
        "categories": categories,
        "companies": companies,
        "page": page,
        "latest_posts": latest_posts,
        "s_form": s_form,
    }
    return render(request, "jobs/index.html", context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    categories = Category.objects.all()
    similar_jobs = Job.objects.filter(jobcategory=job.jobcategory).exclude(id=job.id)[
        :4
    ]

    # subscribing newsletter
    if request.method == "POST":
        s_form = SignUpForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            messages.success(request, "Thank you for subscribing to our newsletter")
            return redirect("jobs:home")
    else:
        s_form = SignUpForm()

    context = {
        "job": job,
        "s_form": s_form,
        "categories": categories,
        "similar_jobs": similar_jobs,
    }
    return render(request, "jobs/job_detail.html", context)


def jobs_by_category(request, slug):
    category = Category.objects.filter(slug=slug).first()
    jobs = Job.objects.filter(jobcategory=category)

    # Newsletter Signup
    if request.method == "POST":
        s_form = SignUpForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            messages.success(request, "Thank you for subscribing to our newsletter")
            return redirect("jobs:home")
    else:
        s_form = SignUpForm()

    # Lookup
    # if query is not None:
    #     lookup = Q(category__icontains=query)
    #     queryset = jobs.filter(lookup).all()

    paginator = Paginator(jobs, 6)
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "jobs": jobs,
        "queryset": queryset,
        "category": category,
        "s_form": s_form,
    }
    return render(request, "jobs/category.html", context)


def jobs_by_company(request, slug):
    companies = Company.objects.all()
    company = companies.filter(slug=slug)[0]
    jobs = Job.objects.filter(company=company)

    context = {
        "jobs": jobs,
        "companies": companies,
        "company": company,
    }

    return render(request, "jobs/company.html", context)


def job_search(request):
    queryset = Job.objects.all()
    query = request.GET.get("q")
    choice = request.GET.get("choice")
    if query != "" and query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if choice != "" and choice is not None and choice != "All Categories":
        queryset = queryset.filter(jobcategory__title__contains=choice)

    paginator = Paginator(queryset, 6)
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "queryset": queryset,
        "query": query,
    }
    return render(request, "jobs/search.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"Thank you {name} for contacting us")

            return redirect("jobs:home")
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "jobs/contact.html", context)


def all_companies(request):
    companies = Company.objects.all()

    query = request.GET.get("q")
    if query != "" and query is not None:
        companies = companies.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )

    jobs = Job.objects.filter(status="published")
    context = {
        "companies": companies,
        "jobs": jobs,
    }
    return render(request, "jobs/companies.html", context)


def all_categories(request):
    categories = Category.objects.all()
    jobs = Job.objects.filter(status="published")
    context = {
        "categories": categories,
        "jobs": jobs,
    }
    return render(request, "jobs/categories.html", context)


def about(request):
    return render(request, "jobs/about.html", context={})


def privacy(request):
    return render(request, "jobs/privacy.html", context={})


def terms_of_service(request):
    return render(request, "jobs/terms_of_service.html", context={})


def error_404(request, exception=None):
    context = {}
    return render(request, "jobs/404.html", context={})


def error_500(request, exception=None):
    context = {}
    return render(request, "jobs/500.html", context={})


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /profile/",
        "Disallow: /login/",
        "Disallow: /logout/",
        "Disallow: /register/",
        "Disallow: /admin/",
        "Disallow: /api/",
        "Disallow: /api-auth/",
        "Disallow: /password_reset/",
        "Sitemap: https://jobsearchke.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
