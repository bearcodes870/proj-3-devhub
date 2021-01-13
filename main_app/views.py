from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Developer

class DeveloperCreate(CreateView):
    model = Developer
    fields = '__all__'

class DeveloperUpdate(UpdateView):
  model = Developer
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description']

class DeveloperDelete(DeleteView):
  model = Developer
  success_url = '/developers/'
  
def home(request):
    developers = Developer.objects.all()
    return render(request, 'home.html', { 'developers': developers })

def about(request):
    return render(request, 'about.html')

@login_required
def developers_index(request):
    developers = Developer.objects.all()
    return render(request, 'developers/index.html', { 'developers': developers })

@login_required
def developers_detail(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    return render(request, 'developers/detail.html', { 'developer' : developer })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
