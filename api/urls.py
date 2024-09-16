from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('owner/', views.GetPortifolioOwner.as_view()),
    path('services/', views.GetServices.as_view()),
    path('projects/', views.GetProjects.as_view()),
]
