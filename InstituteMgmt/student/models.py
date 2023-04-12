from django.contrib.auth.models import AbstractUser
from django.db import models


# authentication
class User(AbstractUser):
    type_user = models.CharField(max_length=50)


# Create your models here.
class StudentProfile(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    college = models.CharField(max_length=500)
    branch = models.CharField(max_length=200)
    year_graduation = models.CharField(max_length=4)
    batch = models.CharField(max_length=250, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class TrainerProfile(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Assignment(models.Model):
    title_assignment = models.CharField(max_length=400)
    notes = models.TextField()
    end_date = models.DateTimeField()
    batch = models.ForeignKey('student.Batches', on_delete=models.CASCADE)


# class StudyMaterial(models.Model):
#     pass


class Batches(models.Model):
    batch_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    batch_code = models.CharField(max_length=20)


class Announcements(models.Model):
    batch = models.ForeignKey('student.Batches', on_delete=models.CASCADE)
    notes = models.TextField()
