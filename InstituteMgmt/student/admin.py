from django.contrib import admin
from .models import StudentProfile, User, Batches, Announcements, Assignment

# Register your models here.
admin.site.register(StudentProfile)
# admin.site.register(StudyMaterial)
admin.site.register(User)
admin.site.register(Batches)
admin.site.register(Announcements)
admin.site.register(Assignment)
