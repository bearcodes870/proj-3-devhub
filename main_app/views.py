from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Developer, Project

class DeveloperCreate(LoginRequiredMixin, CreateView):
    model = Developer
    fields = ['name', 'description']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class DeveloperUpdate(LoginRequiredMixin, UpdateView):
  model = Developer
  fields = ['description']

class DeveloperDelete(LoginRequiredMixin, DeleteView):
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

@login_required
def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', { 'projects': projects})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/developers/create')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def assoc_project(request, developer_id, project_id):
  Developer.objects.get(id=developer_id).projects.add(project_id)
  return redirect('detail', developer_id=developer_id)