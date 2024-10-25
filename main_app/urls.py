from django.urls import path
from . import views # import views from current directory

urlpatterns  = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cat-index'),
]