from django.db.models import Avg, Count, Q
from django.shortcuts import render, redirect, loader
from django.http import HttpResponse
from .models import Student
from .models import Book, Publisher, Author, Store
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from django.views import View
from .forms import EmployeeForm
from .models import Employee
from django.forms import BaseFormSet
from django.forms import formset_factory
from .forms import EmployeeModelForm
from .decorator import wellcome_decorator


# Create your views here.


@require_http_methods(['POST'])
def decorator_check(request):
    return HttpResponse('require_http_methods Decorator')


@wellcome_decorator
def home(request):
    print("View Called")
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


def response_error_handler(request, exception=None):
    return HttpResponse("Response Error Occurred", status=403)


def permission_denied_view(request):
    return PermissionDenied


class EmployeeFormView(View):

    def post(self, request):
        emp_form = EmployeeForm(request.POST)
        if emp_form.is_valid():
            employee = Employee(name=request.POST['name'], email=request.POST['email'], salary=request.POST['salary'])
            employee.save()
            return redirect('home')

    def get(self, request):
        emp_form = EmployeeForm()
        template = loader.get_template('employee_form.html')
        context = {
            'form': emp_form,
        }
        return HttpResponse(template.render(context, request))

    def dispatch(self, request, *args, **kwargs):
        pass

    def put(self, request):
        pass


class EmployeeFormSetView(View):

    def get(self, request):
        employee_form_set = formset_factory(EmployeeForm, absolute_max=2000)
        data = {
            "form-TOTAL_FORMS": "9",
            "form-INITIAL_FORMS": "0",
            "form-0-email": 'a@gmail.com',
            "form-1-email": 'a@gmail.com',
        }
        form_set = employee_form_set(data)
        print(len(form_set.forms))
        print(form_set.absolute_max)
        print(form_set.max_num)
        print(form_set.is_valid())
        for form in form_set:
            print(form.as_table)
        template = loader.get_template("form_set.html")
        return HttpResponse(template.render({'form_set': form_set}, request))


def edit_employee(request):
    employee = Employee.objects.get(pk=1)
    form = EmployeeModelForm(instance=employee)
    template = loader.get_template("form_set.html")
    if request.method == "POST":
        pass
    return HttpResponse(template.render({'form': form}, request))




