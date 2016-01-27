from django.forms.models import ModelForm
from .models import *


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'username', 'password', 'subject')
        
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ('name','description', 'dean')
        
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('name','faculty')
        
#student1 related forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'mname', 'lname','DoBirth', 'phone', 'address', 'guardian', 'guardian_phone', 'classroom')
        
  
class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ('name','level')
        
class ClassroomForm(ModelForm):
    class Meta:
        model = ClassRoom
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
        
