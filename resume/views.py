from django.shortcuts import render


def home(request):
    return render(request, "resume/index.html", context={})

