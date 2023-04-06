from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),

    # For Creating Entry inside DB
    path('add_student_form/', views.add_student_form, name='add_student_form'),
    path('addStudent/', views.add_student, name='add_student'),

    # to read data from DB
    path('student_list/', views.student_list, name='student_list'),
    path('student_details/<int:pk>', views.student_details, name='student_details'),

    # to Update perticular data from DB
    path('update_student_form/<int:pk>', views.update_student_form, name='update_student_form'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),

    # to delete entry from DB
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),

]
