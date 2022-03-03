from django.db import models

# Create your models here.

class Image(models.Model):
    path = models.CharField(max_length=255)
    predicted_label = models.CharField(max_length=100)