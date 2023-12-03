from django.db import models

# Create your models here.

class Car(models.Model):
    VIBOR = (('white', 'white'), ('black', 'black'), ('blue', 'blue'), ('red', 'red'))
    brand = models.CharField(max_length=20, verbose_name='марка', blank=True)
    cost = models.IntegerField(verbose_name='цена', blank=True)
    year = models.IntegerField(verbose_name='год выпуска', blank=True)
    color = models.CharField(max_length=20, choices=VIBOR, verbose_name='цвет', blank=True)


class Company(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название компании')

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Продукт', blank=True)
    cost = models.IntegerField(verbose_name='Цена', blank=True)
    firma = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    title = models.CharField(max_length=10)
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Student(models.Model):
    kurs = models.ManyToManyField(Course)
    name = models.CharField(max_length=20, verbose_name='Имя', blank=True)
    group = models.CharField(max_length=4, verbose_name='Группа', blank=True)
    receives_scholarship = models.BooleanField(max_length=20, verbose_name='Стипендия', blank=True)
    average_score = models.FloatField(max_length=20, verbose_name='Средний бал', blank=True)

    # вывод информации для студента
    def kursDisply(self):
        result = ', '.join([one.title for one in self.kurs.all()])
        return result

    # команда для замены названия таблицы на сайте
    kursDisply.short_description = 'Курсы'

    def __str__(self):
        return f'{self.name}'





