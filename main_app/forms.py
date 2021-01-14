from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['project_name', 'project_overview', 'languages']