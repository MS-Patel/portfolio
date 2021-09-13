from django.shortcuts import render

# Create your views here.


def dummytextblog(request):
    return render(request, 'dummytextblog.html')

def EsEmnOF(request):
    return render(request, 'EsEmnOF.html')

def css_specificityblog(request):
    return render(request, 'css_specificityblog.html')

def fontsblog(request):
    return render(request, 'fontsblog.html')

def colorsblog(request):
    return render(request, 'colorsblog.html')
