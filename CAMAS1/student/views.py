from django.shortcuts import render, redirect, render_to_response,\
    get_object_or_404
from django.template.context_processors import request
from student.models import *
from student.forms import *

# Create your views here.
def students_list(request, is_active = True):
    students = Student.objects.filter(status = is_active)
    return render(request, 'student/students_list.html', {'students':students, 'is_active':is_active})

def student_profile(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/profile.html', {'student': student})
    
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student')
    else:
        form = StudentForm()
        return render(request, 'student/register.html', {'form':form})
    

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.registered_by = request.user
            student.last_updated = timezone.now()
            student.save()
            return redirect('student.views.students_profile', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student/edit_student.html', {'form':form})
    

def deactivate_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.status = False
        student.last_updated = timezone.now()
        student.save()
    return redirect('student.views.students_profile', pk=student.pk)


