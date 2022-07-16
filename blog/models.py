from distutils.command import upload
from django.db import models
from django.urls import reverse
# Create your models here.
# this blog is using the 

#this model is for the header that will appear the upper part of the blog. It has some words and an image
class Header(models.Model):
    headerwords = models.CharField(max_length=500)
    headerpic = models.ImageField(upload_to='images', blank=True)
    
    def __str__(self):
        return self.headerwords
    
STATUS = (
    (0, "Draft"),
    (1, "Published")
)
# Model for the post object in our blog
class Post(models.Model):
    title = models.CharField(max_length=500)
    byline = models.CharField(max_length=500, help_text="Just a small summary or main point of the post")
    slug = models.SlugField()
    post_image = models.ImageField(upload_to='images', blank=True)
    text = models.TextField()
    published = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-published']
    
        
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        #this is a string to represent the model object
        return self.title
    