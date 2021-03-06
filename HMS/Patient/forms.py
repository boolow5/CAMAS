from django.forms.models import ModelForm
from Patient.models import Patient
from django.forms.fields import CharField
from django.forms.widgets import TextInput

class patientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('full_name', 'address', 'phone', 'is_in_patient', 'has_chronic_disorders')
        
