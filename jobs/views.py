from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "jobs/index.html", context)
