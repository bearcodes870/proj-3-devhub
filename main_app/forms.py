from django.forms import ModelForm
from .models import Developer, User, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_overview', 'languages']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ('name', 'description')
