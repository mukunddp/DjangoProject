from django.urls import path

from . import views

urlpatterns = [
    # Home Page
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

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assignments/', views.assignments, name='assignments'),
    path('announcements/', views.announcements, name='announcements'),
    path('overview/', views.overview, name='overview'),
    path('batch/', views.overview, name='batch'),

    # trainer
    path('add_trainer_form/', views.add_trainer_form, name='add_trainer_form'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('trainer_details/<int:pk>', views.trainer_details, name='trainer_details'),
    path('delete_trainer/<int:pk>', views.delete_trainer, name='delete_trainer'),

    path('add_batches/', views.add_batches, name='add_batches'),
    path('registered_list/', views.registered_list, name='registered_list'),
    path('view_student_details/<int:pk>', views.view_student_details, name='view_student_details'),
    path('add_student_batch/<int:pk>', views.add_student_batch, name='add_student_batch'),
    path('student_list_batch/', views.student_list_batch, name='student_list_batch'),


]
