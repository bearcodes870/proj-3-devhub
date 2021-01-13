from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

LANGUAGES = (
    ('J', 'JavaScript'),
    ('H', 'HTML5'),
    ('C', 'CSS3'),
    ('P', 'Python'),
    ('S', 'SQL'),
    ('M', 'MongoDB')
)

class Project(models.Model):
    project_name = models.CharField(max_length=300)
    project_overview = models.CharField(max_length=2000)
    languages = models.CharField(
        max_length=6,
        choices=LANGUAGES
    )

    def __str__(self):
        return self.project_name

class Developer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"developer_id": self.id})
    