from django.shortcuts import render
from . models import Project
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, "Your message was submitted successfully!")
                return HttpResponseRedirect(reverse_lazy('contact'))
        else:
                messages.error(request, 'Something went wrong with your submission. Please try again.')
                # Optionally, you can pass the form with errors to the template
                return render(request, 'contact/contact.html', {'form': form})
    else:
            form = ContactForm()

    return render(request, 'contact.html', {'form': form})
