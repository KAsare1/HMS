from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
)
PATIENT_TYPE = (
    ('PRIVATE', 'PRIVATE'),
    ('COOPERATE', 'COOPERATE')
)


class RegistrationPage(models.Model):
    Name = models.CharField(max_length=60)
    Patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(choices=GENDER, max_length=7) 
    Location = models.CharField(max_length=30)
    Tel = models.IntegerField()

class Appointment(models.Model):
    Name = models.CharField( max_length=60)
    Date_of_Appointment = models.DateField()
    Time_of_Appointment = models.TimeField()
    Doctor_Assigned_to = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE, limit_choices_to={'groups': '8'})
    

class Doctors(models.Model):
    doctors = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE, limit_choices_to={'groups': '8'}, null=True)

class CheckIn(models.Model):
    patient = models.ForeignKey(RegistrationPage, on_delete=models.CASCADE, null=False)
    DoctorAssigned = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE, limit_choices_to={'groups': '8'}, null=True)
    check_in_time = models.DateTimeField(auto_now_add=True, null=True)
    check_out_time = models.DateTimeField(null=True)

class NursesPage(models.Model):
    patient = models.ForeignKey(CheckIn, on_delete=models.CASCADE, null=True)
    Blood_Pressure = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Temperature = models.CharField(max_length=10)
    Pulse_rate = models.CharField(max_length=10)
    Height = models.CharField(max_length=10, null=True)

class Doctorpage(models.Model):
    Name = models.ForeignKey(NursesPage, on_delete=models.CASCADE, null=True)
    complaints = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    findings = models.CharField(max_length=300)
    drugs_assigned = models.CharField(max_length=500)

class Labtechnician(models.Model):
    Name = models.ForeignKey(Doctorpage, on_delete=models.CASCADE, null=True)
    results = models.CharField(max_length=200)


class Pharmacist(models.Model):
    Name = models.ForeignKey(Doctorpage, related_name='patient', on_delete=models.CASCADE, null=True)
    drugs_assigned2 = models.ForeignKey(Doctorpage, related_name='drugs_assigned2',on_delete=models.CASCADE, null=True)
    Number_of_strips2 = models.IntegerField()


class PatientData(models.Model):
    Name = models.ForeignKey(RegistrationPage, max_length=60, on_delete=models.CASCADE)
    Patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE)
    Patient_ID = models.IntegerField()
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(choices=GENDER, max_length=7) 
    Location = models.CharField(max_length=30)
    Tel = models.IntegerField()

