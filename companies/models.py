# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from utils.models import CMPModel


class Company(CMPModel):
    """Company model

    Model that stores the companies information
    """

    name = models.CharField(max_length=100)
    business_id = models.CharField(
        max_length=12,
        unique=True,
        error_messages={
            'unique': _('A Company with the same business ID already exists')
        },
        primary_key=True
    )

    email = models.EmailField(
        max_length=100,
        blank=True,
    )

    phone_number = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='companies/logos', blank=True, null=True)

    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)

    class Meta(CMPModel.Meta):
        """Meta class."""
        ordering = ['-name', '-business_id']

    def __str__(self):
        """Return username"""
        return self.name

    def get_short_name(self):
        """Return username"""
        return self.name
