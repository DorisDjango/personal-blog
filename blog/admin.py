from email.header import Header
from django.contrib import admin


from .models import Header, Post

# Register your models here.
admin.site.register(Header)
admin.site.register(Post)