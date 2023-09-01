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


# Create your views here.


def home(request):
    objects = DateTime.objects.all()
    for obj in objects:
        obj.format = 'PTC'
        obj.save()
    return HttpResponse("Home")
