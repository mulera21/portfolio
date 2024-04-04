from django.shortcuts import render
from . models import Project

# Create your views here.


def index(request):
    context = {}
    return render(request, "main.html", context)


def work(request):
    fetch = Project.objects.all()
    context = {
        fetch: "fetch"
    }
    return render(request, "projects.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)
