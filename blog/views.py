


from django.shortcuts import render
from .models import Header, Post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    model = Post
    #I could use template_name to tell django which template to use, but in its absence,
    # django will infer one from the objects name, so in this case, it will be
    # 'blog/post_list.html'
    template_name = 'home.html'
