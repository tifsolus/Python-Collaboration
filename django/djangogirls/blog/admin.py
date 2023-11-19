''' 
@Program: admin
@Author: Donald Osgood
@Last Date: 2023-11-18 19:14:16
@Purpose:Donald Osgood
'''
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
