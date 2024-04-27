"""Clinic histories model"""

# Django
from django.db import models

# Models
from companies.models import Company
from patients.models.patients import Patient

# Utilities
from utils.models import CMPModel


class ClinicHistory(CMPModel):
    """Clinic history model

    A model that contains the relationship between the Patient and the Company
    TODO:
        Create the ClinicHistoryItems model that will contain the clinical information for the patient
    """

    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Clinic Histories"


class ClinicHistoryItems(CMPModel):
    """Clinic history items model

    A model that contains the clinical information for the patient
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    clinic_history = models.ForeignKey(
        ClinicHistory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Clinic History Items"
