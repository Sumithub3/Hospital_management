# Generated by Django 3.2.13 on 2022-05-31 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal', '0004_auto_20220531_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipd_patient_beds',
            name='name',
            field=models.CharField(choices=[('A1', 'A2'), ('C2', 'C2'), ('D1', 'D1')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient_department_ipd',
            name='bed_allot',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_portal.ipd_patient_beds'),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='pid',
            field=models.CharField(default='AB176949', max_length=8, unique=True),
        ),
    ]
