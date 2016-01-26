from django.contrib import admin
from university.models import *
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Faculty)
admin.site.register(Department)

#student1 related items
admin.site.register(Student)
admin.site.register(Year)
admin.site.register(ClassRoom)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Bill)
admin.site.register(Term)
admin.site.register(Subject)