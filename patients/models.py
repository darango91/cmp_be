# Django
from django.db import models


class Patient(models.Model):
    personal_id = models.IntegerField(
        unique=True,
        error_messages={"unique": "A user with the same personal ID already exists"},
        primary_key=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

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

        ordering = ['-personal_id']
