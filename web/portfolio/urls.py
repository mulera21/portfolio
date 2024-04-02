from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("project/<str:pk>/", views.projects, name="projects"),
    path("contact/<str:pk>/", views.contact, name="contact")

    ]