# Generated by Django 4.0.4 on 2022-05-28 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Oxygengen_beds_total',
            new_name='Oxygen_beds_total',
        ),
    ]
