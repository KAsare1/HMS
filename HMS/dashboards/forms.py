from django import forms
from .models import NursesPage, Doctorpage, Labtechnician, Appointment

class NursesForms(forms.ModelForm):
    class Meta:
        model = NursesPage
        fields = {
            'Temperature',
            'Blood_Pressure',
            'Weight',
            'Pulse_rate'
        }

class DoctorForms(forms.ModelForm):
    class Meta:
        model = Doctorpage
        fields = {
            'complaints',
            'findings',
            'comments',
            'drugs_assigned'
        }

class LabtechForms(forms.ModelForm):
    class Meta:
        model = Labtechnician
        fields = {
            'results',
        }

class AppointmentForms(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = {
            'Name',
            'Date_of_Appointment',
            'Doctor_Assigned_to',
        }
