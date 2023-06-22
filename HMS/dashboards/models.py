from django.db import models

# Create your models here.
class FDEPage(models.Model):
    Name = models.CharField(max_length=60)
    Age = models.IntegerField()
    Date_Of_Birth = models.CharField(max_length=20)
    Location = models.CharField(max_length=30)
    Tel = models.IntegerField()
    
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