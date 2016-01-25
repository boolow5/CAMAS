from django.contrib import admin
from student.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Year)
admin.site.register(Class)
admin.site.register(ClassRoom)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Bill)
admin.site.register(Term)