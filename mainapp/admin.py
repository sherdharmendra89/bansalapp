from django.contrib import admin
from .models import Student, School

admin.site.register(School)
admin.site.register(Student)