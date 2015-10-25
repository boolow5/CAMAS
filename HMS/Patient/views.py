from django.shortcuts import render, redirect, render_to_response

from .models import Patient, Doctor, Appointment
from Patient.forms import patientForm
from django.utils import timezone
from django.contrib.redirects.models import Redirect
from django.template.context import RequestContext

# Create your views here.
def patient_list(request):
    patient_type = 'all'
    patients = Patient.objects.all()
    return render(request, 'Patient/list.html', {'patients':patients, 'patient_type':patient_type})
    
def patient_profile(request, pk):
    patient = Patient.objects.get(pk=pk)
    return render(request, 'Patient/profile.html', {'patient':patient, 'patient_type':patient_type}) 

def in_patient(request):
    patient_type = 'in'
    patients = Patient.objects.filter(is_in_patient=True)
    return render(request, 'Patient/list.html', {'patients':patients, 'patient_type':patient_type})

def out_patient(request):
    patient_type = 'out'
    patients = Patient.objects.filter(is_in_patient=False)
    return render(request, 'Patient/list.html', {'patients':patients, 'patient_type':patient_type})

def register_patient(request):
    patient_type = 'new'
    if request.method == 'POST':
        form = patientForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.save()
            return redirect('Patient.views.patient_list')
    else:
        form = patientForm()
        return render(request, 'Patient/register.html', {'form':form, 'patient_type':patient_type})

