from django.db import models

# Create your models here.
class NursesPage(models.Model):
    Blood_Pressure = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Temperature = models.CharField(max_length=10)
    Pulse_rate = models.CharField(max_length=10)

class Doctorpage(models.Model):
    