from django.db import models

# Create your models here.
class NursesPage(models.Model):
    Height = models.FloatField(max_length=5)