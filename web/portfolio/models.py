from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to="projects", blank=True)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.title