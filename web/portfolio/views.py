from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "main.html", context)


def projects(request, pk):
    context = {}
    return  render(request, "project.html", context)


def contact(request, pk):
    context = {}
    return render(request, "contact.html", context)
