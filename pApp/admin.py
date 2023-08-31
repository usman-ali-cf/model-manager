from django.contrib import admin
from .models import Employee, DateTime


# Register your models here.

@admin.register(DateTime)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class PersonAdmin(admin.ModelAdmin):
    pass
