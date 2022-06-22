# Generated by Django 4.0.4 on 2022-05-28 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_facility_alter_hospital_address_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='hospital.facility')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='hospital.hospital')),
            ],
        ),
    ]
