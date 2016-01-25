from django.forms.models import ModelForm
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'mname', 'lname','DoBirth', 'phone', 'address', 'guardian', 'guardian_phone', 'classroom')
        
class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ('level','description')
        
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
        fields = ('number','balance')
        
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ('payee','amount','description','is_debit')

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'description')
        
