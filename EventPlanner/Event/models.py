from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    date = models.DateField(max_length=50)
    location = models.CharField(max_length=100)
