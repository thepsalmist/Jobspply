from django.shortcuts import render

from .models import Course


def home(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "courses/home.html", context)
