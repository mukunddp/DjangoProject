from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    # For Creating Entry inside DB
    path('add_student_form/', views.add_student_form, name='add_student_form'),
    path('addStudent/', views.add_student, name='add_student'),

    # to read data from DB
    path('student_list/', views.student_list, name='student_list')
]
