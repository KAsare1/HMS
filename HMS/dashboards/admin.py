from django.contrib import admin
from .models import Appointment, NursesPage, Doctorpage, PatientData, RegistrationPage, Labtechnician

admin.site.register(Appointment)
admin.site.register(PatientData)
admin.site.register(NursesPage)
admin.site.register(RegistrationPage)
admin.site.register(Labtechnician)
admin.site.register(Doctorpage)
# Register your models here.
