from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "main.html", context)


def work(request):
    context = {}
    return render(request, "projects.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)
