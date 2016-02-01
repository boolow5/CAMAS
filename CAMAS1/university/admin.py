from django.contrib import admin
from university.models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Position)

#student1 related items
admin.site.register(Student)
admin.site.register(Year)
admin.site.register(Classroom)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Bill)
admin.site.register(Term)
admin.site.register(Subject)

admin.site.register(ExamType)
admin.site.register(Exam)
admin.site.register(ExamReport)
