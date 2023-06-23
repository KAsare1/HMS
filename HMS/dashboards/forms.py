from django import forms
from .models import NursesPage, Doctorpage, Labtechnician, Appointment, RegistrationPage, PatientData
class NursesForms(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = {
            'Temperature',
            'Blood_Pressure',
            'Weight',
            'Pulse_rate'
        }

class DoctorForms(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = {
            'complaints',
            'findings',
            'comments',
            'drugs_assigned'
        }

class LabtechForms(forms.ModelForm):
    class Meta:
        model = PatientData
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
        model = PatientData
        fields = {
            'Name',
            'Patient_type',
            'Date_Of_Birth',
            'Gender',
            'Location',
            'Tel'
        }