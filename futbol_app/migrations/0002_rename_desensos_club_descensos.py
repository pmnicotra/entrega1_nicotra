# Generated by Django 4.0.5 on 2022-06-22 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbol_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='desensos',
            new_name='descensos',
        ),
    ]
