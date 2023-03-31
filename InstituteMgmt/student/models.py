from django.db import models


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


class Assignment(models.Model):

    pass


class StudyMaterial(models.Model):

    pass


class Batches(models.Model):

    pass


class Announcements(models.Model):

    pass
