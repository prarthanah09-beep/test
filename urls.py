from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]