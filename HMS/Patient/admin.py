from django.contrib import admin
from . import views,models

# Register your models here.
admin.site.register(views.Patient)
admin.site.register(views.Doctor)
admin.site.register(views.Appointment)
