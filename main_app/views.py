from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Developer

class User: 
  def __init__(self, name):
    self.name = name

users = [
  User('Lolo'),
  User('Sachi'),
  User('Raven')
]

def home(request):
    developers = Developer.objects.all()
    return render(request, 'home.html', { 'developers': developers })

def about(request):
    return render(request, 'about.html')

def developers_index(request):
    developers = Developer.objects.all()
    return render(request, 'developers/index.html', { 'developers': developers })

def developers_detail(request, developer_id):
    developers = Developer.objects.get(id=developer_id)
    return render(request, 'developers/detail.html', { 'developers' : developers })

