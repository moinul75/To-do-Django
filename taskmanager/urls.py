from django.urls import path
from django.contrib import admin
from . import views

#change the admin dashboard 
admin.site.site_title = "Task Manager"
admin.site.site_header = "Task Manager"
admin.site.index_title = "Welcome to the Task Manager Portal"


urlpatterns = [
    path('',views.Home, name='Home')
]
