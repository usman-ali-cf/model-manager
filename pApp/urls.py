from django.contrib import admin
from django.urls import path, include
from .views import home, student_list,  get_student_by_email
from .views import adult_students, adult_students_values, adult_students_value_list, get_books


urlpatterns = [
    path('', home, name='home'),
    path('students', student_list, name='students'),
    path('books', get_books, name='books'),
    path('adult_students', adult_students, name='adult-students'),
    path('adult_students_values', adult_students_values, name='adult-students-values'),
    path('adult_students_value_list', adult_students_value_list, name='adult-students-value-list'),
    path('students/<str:email>', get_student_by_email, name='student-by-email')

]
