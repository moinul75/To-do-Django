from django.shortcuts import render,HttpResponse
from .serializers import TodoSerializer
from rest_framework import viewsets
from .models import Todo

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello, This is python Server</h1>")

#lets create the model views for this serializers 
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()