from django.forms.models import ModelForm
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'username', 'password', 'subject')

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('name', 'description', 'level')

        
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ('name','description', 'dean')
        
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('name','faculty')
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ('name','description')
#student1 related forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name','DateOfBirth', 'phone', 'address', 'guardian', 'guardian_phone', 'classroom', 'status')
        
  
class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ('name','level')
        
class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ('name','current_year','current_semester','max_year', 'status')
        
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('number', 'owner')
        
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ('payee','amount','description')

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'description')

class ExamTypeForm(ModelForm):
    class Meta:
        model = ExamType
        fields = ('name', 'max_marks')
        
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ('title', 'description', 'starting_date', 'e_type', 'is_admission')

class ExamReportForm(ModelForm):
    class Meta:
        model = ExamReport
        fields = ('exam', 'subject', 'student', 'grade', 'note')
