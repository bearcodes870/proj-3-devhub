from django.shortcuts import render

from django.http import HttpResponse

class User:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name):
    self.name = name

users = [
  User('Lolo'),
  User('Sachi'),
  User('Raven')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_index(request):
    return render(request, 'users/index.html', { 'users': users })