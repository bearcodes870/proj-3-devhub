from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>similar, but different to existing social media</h1>')