from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        return self.full_name

class Patient(Person):       
    is_in_patient = models.BooleanField(default=False)
    has_chronic_disorders = models.BooleanField(default=False)
    register_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.full_name
        
    
class Doctor(Person):
    def __str__(self):
        return self.full_name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    date = models.DateTimeField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.__str__() + ' wants to see ' + self.doctor.__str__() + ' @ ' + self.date.__str__()
    
