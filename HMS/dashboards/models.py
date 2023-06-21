from django.db import models

# Create your models here.
class NursesPage(models.Model):
    Blood_Pressure = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Temperature = models.CharField(max_length=10)
    Pulse_rate = models.CharField(max_length=10)

class Doctorpage(models.Model):
    complaints = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    findings = models.CharField(max_length=300)
    drugs_assigned = models.CharField(max_length=500)

class Labtechnician(models.Model):
    results = models.CharField(max_length=200)