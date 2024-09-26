from django.db import models

from petstagram.photos.models import Photo


# Create your models here.

class Comment(models.Model):
    text = models.TextField(
        max_length=300,
        help_text='Comment must not exceed 300 characters.'
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publication date and time'
    )
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )
