from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class Carausel(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)