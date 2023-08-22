from django import forms
from django.forms import ModelForm
from .models import Employee

BIRTH_YEAR_CHOICE = ['2000', '2001', '2002']
EMPLOYEE_TYPE = [
    ('full', 'Full Time'),
    ('part', 'Part Time'),
    ('intern', 'Internee')
]


class EmployeeForm(forms.Form):
    name = forms.CharField(
        max_length=40,
        label='Name',
        widget=forms.TextInput(attrs={'size': '40', 'border': 'none'})
    )
    email = forms.EmailField(label='Email')
    salary = forms.IntegerField(label='Salary')
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))
    type = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=EMPLOYEE_TYPE,
    )

    class Media:
        css = {
            'all': ['style.css']
        }
        js = ['index.js']


class EmployeeModelForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'salary', 'email', 'type']
        widgets = {
            'name': forms.Textarea(attrs={"cols": 80, "rows": 20, "size": 50})
        }
