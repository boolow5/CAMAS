from django.shortcuts import render, redirect, render_to_response,\
    get_object_or_404
from django.template.context_processors import request
from django.utils import timezone
from django.contrib.auth import user_logged_in 
from university.models import *
from university.forms import *

# Create your views here.
def index(request):
    if user_logged_in:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')

def teachers_list(request):
    teachers = Teacher.objects.filter(is_active = True)
    return render(request, 'teacher/teachers_list.html', {'teachers':teachers})

def teacher_profile(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teacher/teacher_profile.html', {'teacher': teacher})
    
def register_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TeacherForm()
        return render(request, 'teacher/new_teacher.html', {'form':form})
    

def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.registered_by = request.user
            teacher.last_updated = timezone.now()
            teacher.save()
            return redirect('university.views.teacher_profile', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'teacher/edit_teacher.html', {'form':form})
    

def deactivate_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.status = False
        teacher.last_updated = timezone.now()
        teacher.save()
    return redirect('university.views.teacher_profile', pk=teacher.pk)


#student1 related views
def students_list(request):
    students = Student.objects.all()
    return render(request, 'student/students_list.html', {'students':students})

def student_profile(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/student_profile.html', {'student': student})
    
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
        return render(request, 'student/new_student.html', {'form':form})
    

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.registered_by = request.user
            student.last_updated = timezone.now()
            student.save()
            return redirect('university.views.student_profile', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student/edit_student.html', {'form':form})
    

def deactivate_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.status = False
        student.last_updated = timezone.now()
        student.save()
    return redirect('university.views.students_profile', pk=student.pk)

#payment related views
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cms/accounts')
    else:
        form = AccountForm()
        return render(request, 'account/new_account.html', {'form':form})

def accounts_list(request):
    accounts = Account.objects.all()
    return render(request, 'account/accounts_list.html', {'accounts':accounts})

def account_details(request, pk):
    account = Account.objects.get(pk=pk)
    return render(request, 'account/account_details.html', {'account':account})

def edit_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('university.views.account_details', pk=account.pk)
    else:
        form = AccountForm(instance=account)
    
    return render(request, 'account/edit_account.html', {'form':form, 'account':account})
    
def add_payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            if payment.amount > 0:
                payment.is_debit = True
            elif payment.amount < 0:
                payment.is_debit = False
            else:
                form = TransactionForm()
                return render(request, 'payment/new_payment.html', {'form':form, 'error':"Amount cannot be zero!"})
            acount = Account.objects.get(pk= payment.payee.pk) 
            acount.balance += payment.amount
            payment.received_by = request.user
            payment.save()
            return redirect('university.views.payment_details', pk=payment.pk)
    else:
        form = TransactionForm()
        return render(request, 'payment/new_payment.html', {'form':form})
    
def payments_list(request, pk):
    payments = Transaction.objects.filter(payee = pk)
    owner = Account.objects.get(pk=pk)
    return render(request, 'payment/payments_list.html', {'payments':payments,'owner':owner})

def payment_details(request,pk):
    payment = get_object_or_404(Transaction, pk=pk)
    owner = get_object_or_404(Account, pk=payment.payee.pk)
    return render(request, 'payment/payment_details.html', {'payment':payment, 'owner':owner})

