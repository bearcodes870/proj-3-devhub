from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Developer, Project
from .forms import ProjectForm, UserForm, DeveloperForm

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

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'project_overview', 'languages']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
  
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
    return render(request, 'projects/project_index.html', { 'projects': projects })

@login_required
def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'home.html', { 'project': project })

@login_required
def user_profile(request):
    return render(request, 'profiles/user_profile.html')

class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project


class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['project_name', 'project_overview']

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/projects/'

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

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        developer_form = DeveloperForm(request.POST, instance=request.user.developer)
        if user_form.is_valid() and developer_form.is_valid():
            user_form.save()
            developer_form.save()
            return redirect('/profile')
        else:
            error_message = 'invalid'
    else:
        user_form = UserForm(instance=request.user)
        developer_form = DeveloperForm(instance=request.user.developer)
    return render(request, 'main_app/profile_form.html', {
        'user_form': user_form,
        'developer_form': developer_form
    })
    
@login_required
def assoc_project(request, developer_id, project_id):
  Developer.objects.get(id=developer_id).projects.add(project_id)
  return redirect('detail', developer_id=developer_id)

@login_required
def unassoc_project(request, developer_id, project_id):
    Developer.objects.get(id=developer_id).projects.remove(project_id)
    return redirect('detail', developer_id=developer_id)

@login_required
def dev_projects(request, developer_id):
    projects = Project.objects.all()
    developer = Developer.objects.get(id=developer_id)
    projects_developer_doesnt_have = Project.objects.exclude(id__in = developer.projects.all().values_list('id'))
    return render(request, 'developers/project_add.html', {'projects': projects, 'developer': developer, 'not_assigned': projects_developer_doesnt_have})