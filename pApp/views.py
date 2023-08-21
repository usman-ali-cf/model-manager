from django.db.models import Avg, Count, Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Book, Publisher, Author, Store

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


def get_student_by_email(request, email):
    student = Student.students.get_student_by_email(email=email)
    return HttpResponse(student)


def adult_students_values(request):
    students = Student.students.get_adult_students_values()
    return HttpResponse(students)


def adult_students_value_list(request):
    students = Student.students.get_adult_students_value_list()
    return HttpResponse(students)


def get_books(request):
    book1 = Book.objects.aggregate(Avg('price')).values()
    book2 = Book.objects.annotate(Count('authors'), Count('store'))
    book3 = Author.objects.aggregate(average_rating=Avg("book__rating"))
    highly_rated = Count("book", filter=Q(book__rating__gte=7))
    book4 = Author.objects.annotate(num_books=Count("book"), highly_rated_books=highly_rated)
    context = {
        'book1': book1,
        'book2': book2,
        'book3': book3,
        'book4': book4,
    }
    return HttpResponse(context)
