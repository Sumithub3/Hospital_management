# Generated by Django 3.2.13 on 2022-06-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal', '0007_alter_patient_details_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipd_patient_beds',
            name='name',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2'), ('D1', 'D1')], error_messages={'unique': 'Dublicate Bed Entered'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='pid',
            field=models.CharField(default='AB542136', max_length=8, unique=True),
        ),
    ]
