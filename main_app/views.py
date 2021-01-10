from django.shortcuts import render

from django.http import HttpResponse

class User: 
  def __init__(self, name):
    self.name = name

users = [
  User('Lolo'),
  User('Sachi'),
  User('Raven')
]

def home(request):
    return render(request, 'home.html', { 'users': users })

def about(request):
    return render(request, 'about.html')

def users_index(request):
    return render(request, 'users/index.html', { 'users': users })