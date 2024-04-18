# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

class CMPModel(models.Model):
    """
    Cuidate mas pro base model.

    Acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text=_('Date time on which the object was created.')
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text=_('Date time on which the object was last modified.')
    )

    class Meta:
        """
        Meta options
        """
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class CMPHumanModel(CMPModel):
    """
    Cuidate mas pro person base model.

    Acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following additional attributes:
        + personal_id (DateTime): Store the datetime the object was created.
    """

    personal_id = models.IntegerField(
        unique=True,
        error_messages={
            'unique': _('A user with the same personal ID already exists')
        },
        primary_key=True
    )

    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)

    phone_number = models.CharField(
        max_length=17,
        blank=True
    )

    class Meta:
        """
        Meta options
        """
        abstract = True

        ordering = ['-personal_id']