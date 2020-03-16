from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from collections import Counter
from .models import Job
from blog.models import Post
from marketing.models import SignUp
from marketing.forms import SignUpForm
from users.forms import ContactForm


def get_category():
    categories = []
    jobs = Job.objects.all()
    for job in jobs:
        categories.append(job.category)
        categories = list(set(categories))

    return categories


def home(request):
    jobs = Job.objects.all()
    latest_posts = Post.objects.order_by("-publish")[:3]
    category = get_category()
    paginator = Paginator(jobs, 8)
    page = request.GET.get("page")

    # Newsletter Signup
    if request.method == "POST":
        s_form = SignUpForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            messages.success(request, "Thank you for subscribing to our newsletter")
            return redirect("jobs:home")
    else:
        s_form = SignUpForm()

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        "jobs": jobs,
        "category": category,
        "page": page,
        "latest_posts": latest_posts,
        "s_form": s_form,
    }
    return render(request, "jobs/index.html", context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    category = get_category()

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
        "category": category,
        "s_form": s_form,
    }
    return render(request, "jobs/job_detail.html", context)


def jobs_by_category(request, query=None):
    jobs = Job.objects.all()
    category = get_category()
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
    if query is not None:
        lookup = Q(category__icontains=query)
        queryset = jobs.filter(lookup).all()

    paginator = Paginator(queryset, 6)
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


def job_search(request):
    queryset = Job.objects.all()
    query = request.GET.get("q")
    category = get_category()
    choice = request.GET.get("choice")
    if query != "" and query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if choice != "" and choice is not None and choice != "All Categories":
        queryset = queryset.filter(category=choice)

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
        "category": category,
    }
    return render(request, "jobs/search.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("jobs:home")
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "jobs/contact.html", context)


def all_categories(request):
    return render(request, "jobs/categories.html", context={})


def about(request):
    return render(request, "jobs/about.html", context={})


def privacy(request):
    return render(request, "jobs/privacy.html", context={})


def terms_of_service(request):
    return render(request, "jobs/terms_of_service.html", context={})
