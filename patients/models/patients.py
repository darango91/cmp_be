# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import CMPPersonModel


class Patient(CMPPersonModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(
        'Patient birthday date'
    )

    email = models.EmailField(
        max_length=100,
        blank=True,
        unique=True,
        error_messages={
            'unique': _('A patient with the same email already exists')
        }
    )
    REQUIRED_FIELDS = [
        'personal_id',
        'first_name',
        'last_name',
        'birthday',
    ]

    class Meta(CMPPersonModel.Meta):
        """Meta class."""
        ordering = ['-first_name', '-personal_id']

    def __str__(self):
        """Return username"""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self) -> str:
        """Return username"""
        return self.first_name
