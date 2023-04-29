from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

from .forms import SignUpForm, LoginForm
from .models import StudentProfile, User, TrainerProfile, Batches


# Create your views here.
# Login form
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
            elif user is not None and user.type_user == "trainer":
                login(request, user)
                return redirect('student_list')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


# Register User
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
        user = request.user.id
        users = User.objects.get(id=user)
        s.user_id = users
        s.save()
    return redirect('student_details', request.user.id)


def add_student_form(request):
    return render(request, 'addStudent.html')


# Reading all entry into db
def student_list(request):
    list_student = StudentProfile.objects.all()
    return render(request, 'studentlist.html', {'list_student': list_student})


def add_trainer_form(request):
    return render(request, 'add_trainer_form.html')


def add_trainer(request):
    if request.user.type_user == 'trainer':
        if request.method == 'POST':
            s = TrainerProfile()
            s.name = request.POST.get('name')
            s.gender = request.POST.get('gender')
            s.mobile = request.POST.get('mobile')
            s.email = request.POST.get('email')
            s.dob = request.POST.get('dob')
            user = request.user.id
            users = User.objects.get(id=user)
            s.user_id = users
            s.save()
    return redirect('trainer_details', request.user.id)


def trainer_details(request, pk):
    try:
        trainer = TrainerProfile.objects.get(user_id=pk)
        return render(request, 'trainer_details.html', {'trainer': trainer})
    except:

        return redirect('add_trainer_form')


def delete_trainer(request, pk):
    trainer = TrainerProfile.objects.get(id=pk)
    trainer.delete()
    return redirect('trainer_details', pk)


# Reading all entry into db
def student_details(request, pk):
    try:
        student = StudentProfile.objects.get(user_id=pk)
        return render(request, 'studentdetails.html', {'student': student})
    except Exception as e:
        print(e)
        return redirect('add_student_form')


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


def dashboard(request):
    batches = Batches.objects.all()
    try:
        student = StudentProfile.objects.get(user_id=request.user.id)
        for batch in batches:
            if student.batch == batch.batch_name:
                print(batch.batch_name)
                return render(request, 'dashboard.html', {'batch': batch})
    except:
        return render(request, 'dashboard.html', {'message': 'Ask admin to add into Batch'})
    return render(request, 'dashboard.html', {'batches': batches})


def add_batches(request):
    if request.method == 'POST':
        batch = Batches()
        batch.batch_name = request.POST.get('batch_name')
        batch.batch_code = request.POST.get('batch_code')
        batch.course = request.POST.get('course')
        batch.save()
        return redirect('dashboard')
    return render(request, 'add_batches.html')


def registered_list(request):
    list_student = StudentProfile.objects.all()
    return render(request, 'registered_list.html', {'list_student': list_student})


def view_student_details(request, pk):
    student = StudentProfile.objects.get(id=pk)
    batches = Batches.objects.all()
    return render(request, 'studentdetails.html', {'student': student, 'batches': batches})


def add_student_batch(request, pk):
    if request.method == 'POST':
        student = StudentProfile.objects.get(id=pk)
        student.batch = request.POST.get('batch')
        student.save()
        return redirect('registered_list')


def overview(request):
    student = StudentProfile.objects.get(user_id=request.user.id)
    batches = Batches.objects.all()
    for batch in batches:
        if student.batch == batch.batch_name:
            print(batch.batch_name)
            return render(request, 'overview.html', {'batch': batch})
    return render(request, 'overview.html')


def student_list_batch(request):
    student = StudentProfile.objects.get(user_id=request.user.id)
    batches = Batches.objects.all()
    for batch in batches:
        if student.batch == batch.batch_name:
            list_student = StudentProfile.objects.filter(batch=batch.batch_name)
            return render(request, 'studentlist.html', {'list_student': list_student})


def assignments(request):
    return render(request, 'assignments.html')


def announcements(request):
    return render(request, 'announcements.html')

# def dashboard(request):
#     return render(request, 'dashboard.html')
