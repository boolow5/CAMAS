from django.forms.models import ModelForm
from Patient.models import Patient

class patientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('full_name', 'address', 'phone', 'is_in_patient', 'has_chronic_disorders')