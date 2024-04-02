from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("projects/<str:pk>/", views.work, name="projects"),
    path("contact/<str:pk>/", views.contact, name="contact")

    ]