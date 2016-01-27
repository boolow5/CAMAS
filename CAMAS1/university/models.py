from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name


class Teacher(User):
    subject = models.ForeignKey(Subject, default=None)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    dean = models.ForeignKey(Teacher)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty)
    def __str__(self):
        return self.name

#student1 related models

class Year(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField()
    
    def __str__(self):
        return str(self.name) + ' year'
    
class Term(models.Model):
    is_first = models.BooleanField(default=True)
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
    
class ClassRoom(models.Model):
    name = models.CharField(max_length=30, default='One')
    current_year = models.ForeignKey(Year)
    current_semester = models.ForeignKey(Term)
    date_opened = models.DateField(default= timezone.now)
    max_year = models.IntegerField(default=4)
    status = models.BooleanField(default=True)
    
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
    owner = models.ForeignKey(Student)
    number = models.IntegerField()
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    
    def __str__(self):
        return str(self.owner) + '(' + str(self.number) + ')'

class Transaction(models.Model):
    received_by = models.ForeignKey(User)
    payee = models.ForeignKey(Account)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    date = models.DateTimeField(default = timezone.now)
    description = models.TextField(max_length=300)
    is_debit = models.BooleanField(default=True)
    
    def __str__(self):
        if self.is_debit:
            return '$' + str(self.amount) + ' ' + self.description
        else:
            return "( $" + str(self.amount) + ") " + self.description
    
class Bill(models.Model):
    account = models.ForeignKey(Account)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    description = models.TextField(max_length=300)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return str(self.amount) + " for " + self.description

