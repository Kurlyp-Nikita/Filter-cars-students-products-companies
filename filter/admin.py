from django.contrib import admin
from filter.models import *
# Register your models here.
# admin.site.register(Car)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'year', 'color')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'firma') # команда чтобы смотреть на продку (на странице)
    fields = ('name', 'cost', 'firma') # команда чтобы добавить продукты на странице
    list_display_links = ('name', 'firma') # переход от имени к фирме




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'average_score', 'receives_scholarship', 'kursDisply')






