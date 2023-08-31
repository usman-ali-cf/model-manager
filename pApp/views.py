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

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    return HttpResponse("Home")
