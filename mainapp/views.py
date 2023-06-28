from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer
from rest_framework import generics, status

from .forms import *
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

"""
Use both class mentioned in below is use for API CRUD operations on Students and Schools with ViewSet

"""
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


"""
Use all methods mentioned in below is use for CRUD operations with HTML templates on Students and Schools

"""

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})


def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})

def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    return render(request, 'school_detail.html', {'school': school})




def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school-list')
    else:
        form = SchoolForm()

    return render(request, 'school_form.html', {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    schools = School.objects.all()
    return render(request, 'student_form.html', {'form': form, 'schools': schools})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')
    return render(request, 'delete_student.html', {'student': student})


def update_school(request, school_id):
    school = get_object_or_404(School, id=school_id)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('school-list')
    else:
        form = SchoolForm(instance=school)
    return render(request, 'update_school.html', {'form': form, 'school': school})

def delete_school(request, school_id):
    school = get_object_or_404(School, id=school_id)
    if request.method == 'POST':
        school.delete()
        return redirect('school-list')
    return render(request, 'delete_school.html', {'school': school})


