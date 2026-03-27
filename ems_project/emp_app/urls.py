from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_employee/', views.all_employee, name='all_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('remove_employee/<int:employee_id>/', views.remove_employee, name='remove_employee'),
    path('filter_employee/<int:employee_id>/', views.filter_employee, name='filter_employee'),
]