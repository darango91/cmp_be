"""Patients models admin."""

# Django
from django.contrib import admin

# Custom models
from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Company model admin."""
    list_display = ('name', 'business_id', 'email', 'phone_number')
    search_fields = ('name', 'business_id')
    list_filter = ('city', 'state', 'country')
    ordering = ('name', 'business_id')
