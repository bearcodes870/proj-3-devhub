from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    projects = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"developer_id": self.id})
    