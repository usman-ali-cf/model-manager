from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.


def home(request):
    return HttpResponse("Home :)")


def student_list(request):
    students = Student.students.all()
    str_students = [
        student.first_name + ' ' + student.last_name + '-' + str(student.age) + '\n'
        for student in students
    ]
    return HttpResponse(str_students)


def adult_students(request):
    students = Student.students.get_adult_students()
    str_students = [
        student.first_name + ' ' + student.last_name + '-' + str(student.age) + '\n'
        for student in students
    ]
    return HttpResponse(str_students)
