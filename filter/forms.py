from django import forms
from .models import *




class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('brand', 'cost', 'year', 'color')




class ProductForm(forms.ModelForm):
    # pole = forms.ModelChoiceField(Company.objects.all()) # Выбор для поиска компаний


    class Meta:
        model = Product
        fields = ('firma', 'name', 'cost')




class StudentForm(forms.Form):
    poleCourse = forms.ModelChoiceField(Course.objects.all(), required=False, label='Курс')
    poleStud = forms.ModelChoiceField(Student.objects.all(), required=False, label='Студент')
    poleScholarship = forms.BooleanField(required=False, label='Получает стипендию')
    poleScore = forms.FloatField(required=False, label='Средний бал')




