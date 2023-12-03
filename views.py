from .forms import *
from django.shortcuts import render
from .forms import StudentForm
from .models import Course, Student
# Create your views here.

def index(req):
    return render(req, 'index.html')

def car(req):
    db = Car.objects.all()
    forma = CarForm()
    if req.method == 'POST':
        forma = CarForm(req.POST)
        k1 = req.POST.get('brand')
        k2 = req.POST.get('cost')
        k3 = req.POST.get('year')
        k4 = req.POST.get('color')
        print(k1, k2, k3, k4)
        if k1 and k2:
            db = Car.objects.filter(brand=k1, cost__lte=k2, year=k3, color=k4)
        elif k1:
            db = Car.objects.filter(brand=k1)
        elif k2:
            db = Car.objects.filter(cost__lte=k2)
        elif k3:
            db = Car.objects.filter(year=k3)
        elif k4:
            db = Car.objects.filter(color=k4)
    data = {'forma': forma, 'database': db}
    return render(req, 'car.html', data)


def comp(req):
    db = Product.objects.all()
    forma = CompanyForm()
    if req.method == 'POST':
        forma = CompanyForm(req.POST)
        k1 = req.POST.get('firma')
        k2 = req.POST.get('name')
        k3 = req.POST.get('cost')
        filter_params = {}
        if k1:
            filter_params['firma'] = k1
        if k2:
            filter_params['name'] = k2
        if k3:
            filter_params['cost__lte'] = k3
        db = Product.objects.filter(**filter_params)
    data = {'database': db, 'forma': forma}
    return render(req, 'comp.html', data)


def stud(req):
    db = Course.objects.all()
    forma = StudentForm()
    param = ''
    if req.POST:
        a = req.POST.get('poleCourse')
        b = req.POST.get('poleStud')
        c = req.POST.get('poleScholarship')
        d = req.POST.get('poleGPA')
        if b and not a:
            db = Student.objects.get(id=b).kurs.all()
            param = 'S'
        elif a and not b:
            db = Course.objects.get(id=a).student_set.all()
            param = 'C'

        if c:
            db = db.filter(scholarship=True)
        if d:
            db = db.filter(gpa__gt=d)

    for obj in db:
        if isinstance(obj, Student):
            obj.scholarship = "есть" if obj.scholarship else "нет"

    data = {'database': db, 'forma': forma, 'key': param}
    return render(req, 'stud.html', data)


