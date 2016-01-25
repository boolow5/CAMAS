from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=400)
    address = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name

class Teacher(User):
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
