# Generated by Django 5.1.1 on 2024-10-11 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='locations',
            new_name='location',
        ),
    ]
