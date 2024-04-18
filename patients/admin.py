"""Patients models admin."""

# Django
from django.contrib import admin

# Custom models
from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient model admin."""
    list_display = ('personal_id', 'first_name', 'last_name')
    search_fields = ('personal_id', 'first_name', 'last_name', 'email')
    list_filter = ('personal_id', 'first_name', 'last_name')