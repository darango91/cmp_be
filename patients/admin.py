"""Patients models admin."""

# Django
from django.contrib import admin

# Custom models
from patients.models.patients import Patient
from patients.models.clinic_histories import ClinicHistory


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient model admin."""
    list_display = ('personal_id', 'first_name', 'last_name')
    search_fields = ('personal_id', 'first_name', 'last_name', 'email')
    list_filter = ('personal_id', 'first_name', 'last_name')


@admin.register(ClinicHistory)
class ClinicHistoryAdmin(admin.ModelAdmin):
    """Clinic history model admin."""
    list_display = ('patient',)
    search_fields = ('patient',)
    list_filter = ('patient',)

