from django.db.models import Avg, Count, Q
from django.shortcuts import render, redirect, loader
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from django.views import View
from .models import Employee
from django.forms import BaseFormSet
from django.forms import formset_factory
from .decorator import wellcome_decorator
from .models import DateTime
from .models import DateTimezone


# Create your views here.


def home(request):
    objects = DateTime.objects.all()
    id = 1
    for obj in objects:
        obj.format = 'PST'
        obj.time_id = id
        obj.save()
        id += 1
    return HttpResponse("Home")
