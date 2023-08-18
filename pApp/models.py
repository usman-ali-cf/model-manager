from django.db import models


class StudentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(first_name__contains="m")

    def get_adult_students(self):
        return super().get_queryset().filter(age__gte=18)


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    roll_no = models.CharField(max_length=30, unique=True)
    email = models.EmailField(null=False, unique=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    students = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
