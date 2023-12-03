from django.db import models
# Create your models here.

class Car(models.Model):
    VIBOR=(('white', 'white'), ('black', 'black'), ('red', 'red'), ('blue', 'blue'))
    brand = models.CharField(max_length=20, verbose_name='марка', blank=True)
    cost = models.IntegerField(verbose_name='цена', blank=True)
    year = models.IntegerField(verbose_name='год выпуска', blank=True)
    color = models.CharField(max_length=20, choices=VIBOR, verbose_name='цвет', blank=True)

class Company(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название компании')
    def __str__(self):
        return f'{self.title}'
#
class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='Продукт')
    cost = models.IntegerField(verbose_name='Цена')
    firma = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    def __str__(self):
        return f'{self.title}'

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Ф.И.О. Студента')
    group = models.CharField(max_length=50, blank=True, verbose_name='Группа')
    kurs = models.ManyToManyField(Course, blank=True, verbose_name='Курсы')
    scholarship = models.BooleanField(default=False, blank=True, null=True, verbose_name='Получает стипендию')
    gpa = models.FloatField(blank=True, null=True, verbose_name='Средний балл')

    def kursDisplay(self):
        kurs_titles = ', '.join([one.title for one in self.kurs.all()])
        return kurs_titles
    kursDisplay.short_description = 'Курсы'

    def __str__(self):
        return f'{self.name}'


