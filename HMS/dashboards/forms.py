from django import forms
from .models import NursesPage, Doctorpage, Labtechnician, Appointment, RegistrationPage, CheckIn
class NursesForms(forms.ModelForm):
    class Meta:
        model = NursesPage
        fields = {
            'patient',
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
            'Time_of_Appointment',
            'Doctor_Assigned_to',
        }

class RegisterForms(forms.ModelForm):
    class Meta:
        model = RegistrationPage
        fields = {
            'Name',
            'Patient_type',
            'Date_Of_Birth',
            'Gender',
            'Location',
            'Tel'
        }


class DocCheckIn(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = '__all__'
    