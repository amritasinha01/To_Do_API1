from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations

class ListToDo(generics.ListAPIView):     #Read
    querset = ToDo.objects.all()
    serializers_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):   #Update
    querset = ToDo.objects.all()
    serializers_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView):           #Create
    querset = ToDo.objects.all()
    serializers_class = ToDoSerializer

class DeleteToDo(generics.DestroyAPIView):           #Delete
    querset = ToDo.objects.all()
    serializers_class = ToDoSerializer

