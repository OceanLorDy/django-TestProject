from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/main.html", {})


def home(response, id=None):
    return render(response, "dashboard/base.html", {})


def homepage(request):
    return render(request, 'main/about.html', {})


def about(request):
    return render(request, 'main/about.html', {})
