from typing import Reversible
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def blogs(request):
    return render(request, 'blogs.html')
