from django.urls import path
from .views import create_student
from django.shortcuts import render
from . import views

urlpatterns = [
    path('create/', create_student, name='create_student'),
    path('success/', lambda request: render(request, 'success.html'), name='student_success'),
    path('student/create/', views.create_student, name='create_student'),
    path('student/list/', views.student_list, name='student_list'),
]
