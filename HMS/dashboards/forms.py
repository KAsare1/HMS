from django import forms
from .models import NursesPage, Doctorpage, Labtechnician

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