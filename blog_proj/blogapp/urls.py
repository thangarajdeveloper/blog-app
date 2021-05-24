from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListView, name='blogs'),
    path('blog/<int:id>', BlogDetailView, name='blog'),
    path('addblog/', BlogAdd, name='addblog'),
    path('updateblog/<int:id>', BlogUpdate, name='updateblog'),
    path('deleteblog/<int:id>', BlogDelete, name='deleteblog')
]
