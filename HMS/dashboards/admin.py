from django.contrib import admin
from .models import Appointment, NursesPage, Doctorpage, PatientData, RegistrationPage, Labtechnician, CheckIn, Doctors


admin.site.register(Appointment)
admin.site.register(PatientData)
admin.site.register(NursesPage)
admin.site.register(RegistrationPage)
admin.site.register(Labtechnician)
admin.site.register(Doctorpage)
admin.site.register(CheckIn)
admin.site.register(Doctors)
# Register your models here.
