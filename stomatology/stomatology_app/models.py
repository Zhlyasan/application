from django.db import models

# Create your models here.


class Doctor(models.Model):
  name = models.CharField(max_length=50)
  surname = models.TextField(null=False, blank=True)
  birth_date = models.DateTimeField(null=False, blank=True)
  snils = models.CharField(max_length=14)
  inn = models.CharField(max_length=10)


class Patient(models.Model):
  name = models.CharField(max_length=50)
  surname = models.TextField(null=False, blank=True)
  birth_date = models.DateTimeField(null=False, blank=True)
  allergies = models.CharField(null=False,max_length=100)
  sale = models.IntegerField(max_length=50)

class Session(models.Model):
  doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE)
  patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
  date_time = models.DateTimeField(null=False, blank=True)

class Worklist(models.Model):
  session = models.ForeignKey("Session",on_delete=models.CASCADE)
  name = models.TextField(null=True, blank=True)
  cost = models.FloatField(null=False, blank=True)