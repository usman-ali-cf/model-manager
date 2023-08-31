from django.db import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Employee(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )
    salary = models.IntegerField(null=False)
    email = models.EmailField(null=False, unique=False)


class DateTime(models.Model):
    time = models.DateTimeField(null=True, )
