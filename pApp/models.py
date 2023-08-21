from django.db import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class StudentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(Q(first_name__contains="m") | Q(first_name__contain="m"))

    def get_adult_students(self):
        return super().get_queryset().filter(age__gte=18)

    def get_adult_students_values(self):
        return super().get_queryset().filter(age__gte=18).values()

    def get_adult_students_value_list(self):
        return super().get_queryset().filter(age__gte=18).values_list()

    def get_student_by_email(self, email):
        try:
            return super().get_queryset().get(email=email)
        except ObjectDoesNotExist as e:
            return None


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    roll_no = models.CharField(max_length=30, unique=True)
    email = models.EmailField(null=False, unique=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class_id = models.IntegerField(null=True)
    roll_id = models.IntegerField(null=True)

    objects = models.Manager()
    students = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
