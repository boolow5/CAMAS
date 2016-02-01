from django.shortcuts import render, redirect, render_to_response,\
    get_object_or_404
from django.template.context_processors import request
from university import settings
from django.utils import timezone
from django.contrib.auth import user_logged_in 
from university.models import *
from university.forms import *

# Create your views here.
def index(request):
    if user_logged_in:
        return render(request, 'index.html',{'settings':settings})
    else:
        return render(request, 'login.html')

def teachers_list(request):
    teachers = Employee.objects.filter(is_active = True)
    return render(request, 'teacher/teachers_list.html', {'teachers':teachers,'settings':settings})

def teacher_profile(request, pk):
    teacher = Employee.objects.get(pk=pk)
    return render(request, 'teacher/teacher_profile.html', {'teacher': teacher,'settings':settings})
    
def register_teacher(request):
    error = None
    try:
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = EmployeeForm()
    except:
        error = 'Please enter a valid data before you submit!'
    
    return render(request, 'teacher/new_teacher.html', {'form':form, 'error':error,'settings':settings})

def update_teacher(request, pk):
    error = None
    try:
        teacher = get_object_or_404(Employee, pk=pk)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=teacher)
            if form.is_valid():
                teacher = form.save(commit=False)
                teacher.registered_by = request.user
                teacher.last_updated = timezone.now()
                teacher.save()
                return redirect('university.views.teacher_profile', pk=teacher.pk)
        else:
            form = EmployeeForm(instance=teacher)
    except:
        error = 'Please fill all required fields before you submit!'
    return render(request, 'teacher/edit_teacher.html', {'form':form,'error':error,'settings':settings})
    

def deactivate_teacher(request, pk):
    teacher = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        teacher.status = False
        teacher.last_updated = timezone.now()
        teacher.save()
    return redirect('university.views.teacher_profile', pk=teacher.pk)


#student1 related views
def students_list(request):
    students = Student.objects.all()
    return render(request, 'student/students_list.html', {'students':students,'settings':settings})

def student_profile(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/student_profile.html', {'student': student,'settings':settings})
    
def register_student(request):
    error = None
    try:
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = StudentForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'student/new_student.html', {'form':form, 'error':error,'settings':settings})

def update_student(request, pk):
    error=None
    try:
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
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'student/edit_student.html', {'form':form, 'error':error,'settings':settings})
    

#payment related views
def create_account(request):
    error = None
    try:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/cms/accounts')
        else:
            form = AccountForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'account/new_account.html', {'form':form,'error':error,'settings':settings})

def accounts_list(request):
    accounts = Account.objects.all()
    return render(request, 'account/accounts_list.html', {'accounts':accounts})

def account_details(request, pk):
    account = Account.objects.get(pk=pk)
    return render(request, 'account/account_details.html', {'account':account})

def edit_account(request, pk):
    error = None
    try:
        account = get_object_or_404(Account, pk=pk)
        if request.method == 'POST':
            form = AccountForm(request.POST, instance=account)
            if form.is_valid():
                account = form.save()
                return redirect('university.views.account_details', pk=account.pk)
        else:
            form = AccountForm(instance=account)
    except:
        error = 'Please enter a valid values into the fields!'
    return render(request, 'account/edit_account.html', {'form':form, 'account':account,'error':error,'settings':settings})
    
def add_payment(request):
    form = TransactionForm(request.POST)
    try:
        if request.method == 'POST':
            if form.is_valid():
                payment = form.save(commit=False)
                if payment.amount > 0:
                    payment.is_debit = True
                elif payment.amount < 0:
                    payment.is_debit = False
                else:
                    form = TransactionForm()
                    return render(request, 'payment/new_payment.html', {'form':form, 'error':"Amount cannot be zero!",'settings':settings})
                acount = Account.objects.get(pk= payment.payee.pk) 
                acount.balance += payment.amount
                payment.received_by = request.user
                payment.save()
                acount.save()
                return redirect('university.views.payment_details', pk=payment.pk)
        else:
            form = TransactionForm()
            return render(request, 'payment/new_payment.html', {'form':form})
    except:
        pass
    return render(request, 'payment/new_payment.html', {'form':form,'error':'Please enter valid values for each field!','settings':settings})        
        
def payments_list(request, pk):
    payments = Transaction.objects.filter(payee = pk)
    owner = Account.objects.get(pk=pk)
    return render(request, 'payment/payments_list.html', {'payments':payments,'owner':owner,'settings':settings})

def payment_details(request,pk):
    payment = get_object_or_404(Transaction, pk=pk)
    payment.amount = abs(payment.amount)
    owner = get_object_or_404(Account, pk=payment.payee.pk)
    return render(request, 'payment/payment_details.html', {'payment':payment, 'owner':owner,'settings':settings})

#exam related views
def create_exam(request):
    error = None
    try:
        if request.method == 'POST':
            form = ExamForm(request.POST)
            if form.is_valid():
                exam = form.save()
                return redirect('/cms/exams')
        else:
            form = ExamForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/new_exam.html', {'form':form, 'error':error,'settings':settings})

def exams_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exams_list.html', {'exams':exams,'settings':settings})

def exam_details(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exam/exam_details.html', {'exam':exam,'settings':settings})

def edit_exam(request, pk):
    error = None
    try:
        exam = get_object_or_404(Exam, pk=pk)
        if request.method == 'POST':
            form = ExamForm(request.POST, instance=exam)
            if form.is_valid():
                exam = form.save()
                return redirect('university.views.exam_details', pk=exam.pk)
        else:
            form = ExamForm(instance=exam)
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/edit_exam.html', {'form':form, 'exam':exam, 'error':error,'settings':settings})

#exam types
def create_exam_type(request):
    error = None
    try:
        if request.method == 'POST':
            form = ExamTypeForm(request.POST)
            if form.is_valid():
                exam_type = form.save()
                return redirect('university.views.exam_type_details', pk=exam_type.pk)
        else:
            form = ExamTypeForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/new_exam_type.html', {'form':form, 'error':error,'settings':settings})


def exam_types_list(request):
    exam_types = ExamType.objects.all()
    return render(request, 'exam/exam_types_list.html', {'exam_types':exam_types})

def exam_type_details(request, pk):
    exam_type = ExamType.objects.get(pk=pk)
    return render(request, 'exam/exam_type_details.html', {'exam_type':exam_type})

def edit_exam_type(request, pk):
    error = None
    try:
        exam_type = get_object_or_404(ExamType, pk=pk)
        if request.method == 'POST':
            form = ExamTypeForm(request.POST, instance=exam_type)
            if form.is_valid():
                exam_type = form.save()
                return redirect('university.views.exam_details', pk=exam_type.pk)
        else:
            form = ExamForm(instance=exam_type)
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/edit_exam_type.html', {'form':form, 'exam_type':exam_type, 'error':error,'settings':settings})

#
#exam report
def create_exam_report(request):
    error = None
    try:
        if request.method == 'POST':
            form = ExamReportForm(request.POST)
            if form.is_valid():
                exam_report = form.save()
                return redirect('university.views.exam_report_details', pk=exam_report.pk)
        else:
            form = ExamReportForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/new_exam_report.html', {'form':form, 'error':error,'settings':settings})


def exam_reports_list(request):
    exam_reports = ExamReport.objects.all()
    return render(request, 'exam/exam_reports_list.html', {'exam_reports':exam_reports,'settings':settings})

def exam_report_details(request, pk):
    exam_report = ExamReport.objects.get(pk=pk)
    minimum = (exam_report.exam.e_type.max_marks / 2)
    return render(request, 'exam/exam_report_details.html', {'exam_report':exam_report, 'minimum':minimum,'settings':settings})

def edit_exam_report(request, pk):
    error = None
    try:
        exam_report = get_object_or_404(ExamReport, pk=pk)
        if request.method == 'POST':
            form = ExamReportForm(request.POST, instance=exam_report)
            if form.is_valid():
                exam_report = form.save()
                return redirect('university.views.exam_report_details', pk=exam_report.pk)
        else:
            form = ExamReportForm(instance=exam_report)
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'exam/edit_exam_report.html', {'form':form, 'exam_report':exam_report, 'error':error,'settings':settings})

#
#exam report

def classroom_details(request, pk):
    classroom = Classroom.objects.get(pk=pk)
    return render(request, 'class/classroom_details.html', {'classroom':classroom,'settings':settings})

#subjects
def create_subject(request):
    error = None
    try:
        if request.method == 'POST':
            form = SubjectForm(request.POST)
            if form.is_valid():
                subject = form.save()
                return redirect('university.views.subject_details', pk=subject.pk)
        else:
            form = SubjectForm()
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'subject/new_subject.html', {'form':form, 'error':error,'settings':settings})


def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject/subjects_list.html', {'subjects':subjects,'settings':settings})

def subject_details(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'subject/subject_details.html', {'subject':subject,'settings':settings})

def edit_subject(request, pk):
    error = None
    try:
        subject = get_object_or_404(Subject, pk=pk)
        if request.method == 'POST':
            form = SubjectForm(request.POST, instance=subject)
            if form.is_valid():
                subject = form.save()
                return redirect('university.views.subject_details', pk=subject.pk)
        else:
            form = SubjectForm(instance=subject)
    except:
        error = "Please make sure you entered all required field's data"
        
    return render(request, 'subject/edit_subject.html', {'form':form, 'subject':subject, 'error':error,'settings':settings})

def header_content(request):
    if user_logged_in:
        return render('university/header.html', {'settings':settings,'settings':settings})
    else:
        return redirect("university.views.login_employee")
    
def footer_content(request):
    if user_logged_in:
        return render('university/footer.html')
    