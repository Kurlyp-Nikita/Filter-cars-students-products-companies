from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'cost', 'year', 'color')


class CompanyForm(forms.Form):
    firma = forms.ModelChoiceField(Company.objects.all(), required=False, label='Компания')
    name = forms.CharField(max_length=100, required=False, label='Название сока')
    cost = forms.IntegerField(required=False, label='Цена')


class StudentForm(forms.Form):
    poleCourse = forms.ModelChoiceField(Course.objects.all(), required=False, label='Курс')
    poleStud = forms.ModelChoiceField(Student.objects.all(), required=False, label='Студент')
    poleScholarship = forms.BooleanField(required=False, label='Стипендия')
    poleGPA = forms.DecimalField(required=False, label='Средний балл')