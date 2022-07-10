from distutils.command import upload
from django.db import models

# Create your models here.

#this model is for the header that will appear the upper part of the blog. It has some words and an image
class Header(models.Model):
    headerwords = models.CharField(500)
    headerpic = models.ImageField(upload_to='images', blank=True)
    
    def __str__(self):
        self.headerwords