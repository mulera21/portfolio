from django.shortcuts import render
from . models import Project

# Create your views here.


def index(request):
    context = {}
    return render(request, "main.html", context)


def work(request):
    new = Project.objects.all()
    context = {
        new: "new"
    }
    return render(request, "projects.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)
