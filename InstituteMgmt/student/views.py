from django.shortcuts import render, redirect

from .models import StudentProfile


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


# should add entry into db
def add_student(request):
    if request.method == 'POST':
        s = StudentProfile()
        s.name = request.POST.get('name')
        s.gender = request.POST.get('gender')
        s.mobile = request.POST.get('mobile')
        s.branch = request.POST.get('branch')
        s.college = request.POST.get('college')
        s.email = request.POST.get('email')
        s.dob = request.POST.get('dob')
        s.year_graduation = request.POST.get('grad')
        s.save()
    return redirect('index')


def add_student_form(request):
    return render(request, 'addStudent.html')


def student_list(request):
    list_student = StudentProfile.objects.all()
    return render(request, 'studentlist.html', {'list_student': list_student})
