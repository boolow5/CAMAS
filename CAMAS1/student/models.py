from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from university.models import *

# Create your models here.
class Year(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField()
    
    def __str__(self):
        return str(self.name) + ' year'
    
class Term(models.Model):
    is_first = models.BooleanField(default=True)
    
    def __str__(self):
        if self.is_first:
            return "One"
        else: return "Two"
    
class Class(models.Model):
    level = models.ForeignKey(Year)
    description = models.TextField()
    department = models.ForeignKey(Department)
    
    def __str__(self):
        return str(self.level)
    
class ClassRoom(models.Model):
    name = models.CharField(max_length=30, default='One')
    current_year = models.ForeignKey(Year)
    current_semester = models.ForeignKey(Term)
    date_opened = models.DateField(default= timezone.now)
    max_year = models.IntegerField(default=4)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    DoBirth = models.DateField()
    address = models.TextField(default=None)
    phone = models.CharField(max_length=30)
    guardian = models.CharField(max_length=50)
    guardian_phone = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    registered = models.DateField(default = timezone.now)
    registered_by = models.ForeignKey(User)
    classroom = models.ForeignKey(ClassRoom)
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.fname + " " + self.mname + " " + self.lname



class Account(models.Model):
    number = models.IntegerField()
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    
    def __str__(self):
        return str(self.number)

class Transaction(models.Model):
    received_by = models.ForeignKey(User)
    payee = models.ForeignKey(Student)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    date = models.DateTimeField(default = timezone.now)
    description = models.TextField(max_length=300)
    is_debit = models.BooleanField(default=True)
    
    def __str__(self):
        if self.is_debit:
            return str(self.amount)
        else:
            return "(" + str(self.amount) + ")"
    
class Bill(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    description = models.TextField(max_length=300)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return str(self.amount) + " for " + self.description

