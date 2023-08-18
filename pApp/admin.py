from django.contrib import admin
from .models import Student


# Register your models here.

@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    pass
