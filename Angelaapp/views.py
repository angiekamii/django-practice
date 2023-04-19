from django.shortcuts import render, redirect
from django.http import HttpResponse
from Angelaapp.models import Student
from Angelaapp.forms import StudentForm
from Angelaapp.forms import EmployeeForm


# Create your views here.
def hello(request):
    return HttpResponse("Hello there,Angela")


def evenodd(request):
    x = 25
    if x % 2 == 0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")


def index(request):
    return render(request, 'index.html')


def variables(request):
    details = {
        "firstname": "Angela",
        "lastname": "Mukami",
        "age": 19,
        "place": "Westlands"
    }
    return render(request, 'variables.html', details)


def assignment(request):
    sane = {
        "Employeename": "Susan",
        "Salary": 75000,
        "EmployeeID": 5
    }
    return render(request, 'assignment.html', sane)


def images(request):
    return render(request, 'images.html')


def background(request):
    return render(request, 'background.html')


def members(request):
    all - Student.objects.all().values()
    details = {
        "members": all
    }
    return render(request, 'members.html', details)


def student(request):
    stu = StudentForm()
    return render(request, 'student.html', {'form': stu})


def employee(request):
    if request.method == "post":
        form = EmployeeForm(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EmployeeForm()
        return render(request, 'empolyee.html', {'form': form})


def setsession(request):
    request.session['firstname'] = 'Angela'
    request.session['lastname'] = 'Mukami'
    request.session['Email'] = 'angelajoan138@gmail.com'
    return HttpResponse('Session has been successfully created')


def getsession(request):
    fname = request.session['firstname']
    lname = request.session['lastname']
    emailaddress = request.session['Email']
    return HttpResponse(fname + ' ' + lname + ' ' + emailaddress)

def form(request):
    return render(request, 'form.html')

def company(request):
    return render(request, 'companiesform.html')

