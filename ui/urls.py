from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('gallery/<int:project_id>/', views.gallery, name='gallery')
]
