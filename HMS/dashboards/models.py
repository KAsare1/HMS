from django.db import models

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
    Name = models.CharField(max_length=60)
    Date_of_Appointment = models.DateField()
    Time_of_Appointment = models.TimeField()
    Doctor_Assigned_to = models.CharField(max_length=30)
    
class NursesPage(models.Model):
    Blood_Pressure = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Temperature = models.CharField(max_length=10)
    Pulse_rate = models.CharField(max_length=10)
    Height = models.CharField(max_length=10)

class Doctorpage(models.Model):
    complaints = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    findings = models.CharField(max_length=300)
    drugs_assigned = models.CharField(max_length=500)

class Labtechnician(models.Model):
    results = models.CharField(max_length=200)


class PatientData(models.Model):
    Name = models.CharField(max_length=60)
    Patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(choices=GENDER, max_length=7) 
    Location = models.CharField(max_length=30)
    Tel = models.IntegerField()

    Blood_Pressure = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Temperature = models.CharField(max_length=10)
    Pulse_rate = models.CharField(max_length=10)
    Height = models.CharField(max_length=10)

    complaints = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    findings = models.CharField(max_length=300)
    drugs_assigned = models.CharField(max_length=500)

    results = models.CharField(max_length=200)