from django.shortcuts import render
from .forms import *


def index(req):
    return render(req, 'index.html')


def car(req):
    # 1-й вариант


    # a = Car.objects.get(id=1)# один объект
    # print(a, a.brand)
    #
    # b = Car.objects.filter(color='white')# список из объектов
    # print(b.count())
    # for one in b:
    #     print(one.brand)
    #
    # c = Car.objects.filter(cost__lte=100)
    # print(c.count())
    # for one in c:
    #     print(one.brand)
    #
    # d = Car.objects.exclude(cost__lte=100)
    # print(d.count())
    # for one in d:
    #     print(one.brend)


    # 2-й вариант
    # Car.objects.filter(cost__lte=100).exclude(color='white')


    # 3-й вариант
    forma = CarForm()
    db = {}
    if req.POST:
        forma = CarForm(req.POST)
        k1 = req.POST.get('brand')
        k2 = req.POST.get('cost')
        k3 = req.POST.get('year')
        k4 = req.POST.get('color')
        print(k1, k2, k3, k4)
        if k3:
            db = Car.objects.filter(year=k3)

        if k4:
            db = Car.objects.filter(color=k4)

        if k1 and k2:
            db = Car.objects.filter(brand=k1, cost__lte=k2)

        elif k1:
            db = Car.objects.filter(brand=k1)

        elif k2:
            db = Car.objects.filter(cost__lte=k2)

    data = {'forma': forma, 'database': db}
    return render(req, 'car.html', data)




def comp(req):
    # db = Product.objects.all()

    db = {}
    forma = ProductForm()
    if req.POST:
        k1 = req.POST.get('firma')
        k2 = req.POST.get('name')
        k3 = req.POST.get('cost')
        print(k1, k2, k3)

        if k1:
            db = Product.objects.filter(firma=k1)

        elif not k1:
            db = Product.objects.all()

        if k2:
            db = Product.objects.filter(name=k2)

        if k3:
            db = Product.objects.filter(cost__lte=k3)


        # db = Company.objects.get(id=k1).product_set.all() # добавление продуктов компании

    data = {'database': db, 'forma': forma}
    return render(req, 'comp.html', data)


def stud(req):
    db = Student.objects.all()
    forma = StudentForm()
    param = ''

    if req.POST:
        a = req.POST.get('poleCourse')
        b = req.POST.get('poleStud')
        c = req.POST.get('poleScholarship')
        d = req.POST.get('poleScore')

        if b and not a:
            db = Student.objects.get(id=b).kurs.all()
            # выбрали студента
            param = 'C'

        elif a and not b:
            # student_set команда для связывания таблиц
            db = Course.objects.get(id=a).student_set.all()
            # выбрали курс
            param = 'S'

        if c:
            db = Student.objects.filter(receives_scholarship=True)
            param = 'S'

        if d:
            db = Student.objects.filter(average_score__gte=d)
            param = 'S'

    data = {'database': db, 'forma': forma, 'key': param}
    return render(req, 'stud.html', data)






