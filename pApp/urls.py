from django.contrib import admin
from django.urls import path, include
from .views import home, student_list, get_student_by_email
from .views import adult_students, adult_students_values, adult_students_value_list, get_books
from .views import permission_denied_view, response_error_handler, decorator_check
from .views import EmployeeFormView, EmployeeFormSetView, edit_employee

handler403 = response_error_handler

urlpatterns = [
    path('', home, name='home'),
    path('students', student_list, name='students'),
    path('books', get_books, name='books'),
    path('adult_students', adult_students, name='adult-students'),
    path('adult_students_values', adult_students_values, name='adult-students-values'),
    path('adult_students_value_list', adult_students_value_list, name='adult-students-value-list'),
    path('students/<str:email>', get_student_by_email, name='student-by-email'),
    path('403/', response_error_handler, name='403'),
    path('decorator_check', decorator_check, name='decorator-check'),
    path('employee_form', EmployeeFormView.as_view(), name='employee-form'),
    path('employee_form_set', EmployeeFormSetView.as_view(), name='employee-form'),
    path('employee_edit', edit_employee, name='employee-edit')

]
