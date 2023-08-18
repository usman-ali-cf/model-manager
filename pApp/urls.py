from django.contrib import admin
from django.urls import path, include
from .views import home, student_list, adult_students

urlpatterns = [
    path('', home, name='home'),
    path('students', student_list, name='students'),
    path('adult_students', adult_students, name='adult-students'),

]
