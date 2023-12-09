from django.db import models

# Create your models here.


class Doctor(models.Model):
  name = models.CharField(max_length=50, verbose_name='Имя')
  surname = models.TextField(null=False, blank=True,  verbose_name='Фамилия')
  birth_date = models.DateTimeField(null=False, blank=True, verbose_name='Дата рождения')
  snils = models.CharField(max_length=14, verbose_name='СНИЛС')
  inn = models.CharField(max_length=10, verbose_name='ИНН')
  def __str__(self):
    return f"{self.name} {self.surname}"
  class Meta:
    verbose_name_plural = 'Доктора'
    verbose_name = 'Доктор'
    ordering = ['-surname', '-name']

class Patient(models.Model):
  name = models.CharField(max_length=50,  verbose_name='Имя')
  surname = models.TextField(null=False, blank=True,  verbose_name='Фамилия')
  birth_date = models.DateTimeField(null=False, blank=True, verbose_name='Дата рождения')
  allergies = models.CharField(null=False,max_length=100, verbose_name='Аллергии')
  sale = models.IntegerField(max_length=50, verbose_name='Размер скидки')

  def __str__(self):
    return f"{self.name} {self.surname}"
  class Meta:
    verbose_name_plural = 'Пациенты'
    verbose_name = 'Пациент'
    ordering = ['-surname', '-name']

class Session(models.Model):
  doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE, related_name='doctors', verbose_name= 'Доктор')
  patient = models.ForeignKey("Patient",on_delete=models.CASCADE, related_name='patients', verbose_name= 'Пациент')
  date_time = models.DateTimeField(null=False, blank=True, verbose_name= 'Время записи')

  def __str__(self):
    return f"{self.doctor.name} {self.doctor.surname} {self.patient.name} {self.patient.surname} {self.date_time}"
  class Meta:
    verbose_name_plural = 'Осмотры'
    verbose_name = 'Осмотр'
    ordering = ['date_time']

class Worklist(models.Model):
  session = models.ForeignKey("Session",on_delete=models.CASCADE, related_name='worklists', verbose_name= 'Запись')
  name = models.TextField(null=True, blank=True,  verbose_name= 'Наименование работы')
  cost = models.FloatField(null=False, blank=True,  verbose_name= 'Цена')

  def __str__(self):
    return f"{self.name}"
  class Meta:
    verbose_name_plural = 'Процедуры'
    verbose_name = 'Процедура'
    ordering = ['cost']
