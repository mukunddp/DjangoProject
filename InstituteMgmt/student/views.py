from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

from .forms import SignUpForm, LoginForm
from .models import StudentProfile


# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.type_user == "student":
                login(request, user)
                return redirect('index')
            elif user is not None and user.type_user == "teacher":
                login(request, user)
                return redirect('student_list')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect(reverse('login_view'))
    # return redirect('login_view')


def index(request):
    return render(request, 'index.html')
#
#
# def login(request):
#     return render(request, 'login.html')
#
#
# def register(request):
#     return render(request, 'register.html')


# Creating an entry into db
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


# Reading all entry into db
def student_list(request):
    list_student = StudentProfile.objects.all()
    return render(request, 'studentlist.html', {'list_student': list_student})


# Reading all entry into db
def student_details(request, pk):
    student = StudentProfile.objects.get(id=pk)
    return render(request, 'studentdetails.html', {'student': student})


# Update student page into DB
def update_student_form(request, pk):
    student = StudentProfile.objects.get(id=pk)
    return render(request, 'updatestudent.html', {'student': student})


# Update student details into DB
def update_student(request, pk):
    if request.method == 'POST':
        s = StudentProfile.objects.get(id=pk)
        s.name = request.POST.get('name')
        s.gender = request.POST.get('gender')
        s.mobile = request.POST.get('mobile')
        s.branch = request.POST.get('branch')
        s.college = request.POST.get('college')
        s.email = request.POST.get('email')
        s.dob = request.POST.get('dob')
        s.year_graduation = request.POST.get('grad')
        s.save()
    return redirect('student_details', pk)


def delete_student(request, pk):
    student = StudentProfile.objects.get(id=pk)
    student.delete()
    return redirect('student_list')
