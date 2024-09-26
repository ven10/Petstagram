from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import FileSizeValidator


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=[
            FileSizeValidator(5)
        ],
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ],
        blank=True,
        null=True,
        help_text='Comment must not exceed 300 characters.'
    )

    locations = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return f"Photo {self.id} - {self.description}"