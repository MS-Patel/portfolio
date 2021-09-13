from django.urls import path
from . import views

urlpatterns = [
    path('dummytextblog', views.dummytextblog, name='dummytextblog'),
    path('EsEmnOF', views.EsEmnOF, name='EsEmnOF'),
    path('fontsblog', views.fontsblog, name='fontsblog'),
    path('colorsblog', views.colorsblog, name='colorsblog'),
    path('css_specificityblog', views.css_specificityblog, name='css_specificityblog'),
    
]
