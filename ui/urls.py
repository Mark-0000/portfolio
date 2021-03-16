from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('', views.home, name='index'),
    path('gallery/<int:project_id>/', views.gallery, name='gallery')

]
