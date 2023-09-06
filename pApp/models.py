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
    time_id = models.IntegerField(null=False, default=1)
    time = models.DateTimeField(null=True, )
    format = models.CharField(null=True, default='PST', max_length=30)


class DateTimezone(models.Model):
    zone = models.CharField(null=False, default="UTC", max_length=30)
