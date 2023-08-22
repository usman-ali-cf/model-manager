from django.contrib import admin
from .models import Student, Employee


# Register your models here.

@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class PersonAdmin(admin.ModelAdmin):
    pass
