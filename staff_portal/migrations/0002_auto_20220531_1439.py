# Generated by Django 3.2.13 on 2022-05-31 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift_in_timings',
            name='entry',
            field=models.TimeField(default=datetime.time(14, 39, 12, 205677)),
        ),
        migrations.AlterField(
            model_name='shift_out_timings',
            name='out',
            field=models.TimeField(default=datetime.time(14, 39, 12, 205677)),
        ),
    ]
