from django.contrib import admin
from .models import *
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'date_time']

@admin.register(Worklist)
class WorklistAdmin(admin.ModelAdmin):
    list_display = ['session', 'name']

