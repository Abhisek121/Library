# Generated by Django 3.2.9 on 2021-12-05 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_alter_record_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2021, 12, 5, 6, 55, 24, 789928)),
        ),
    ]
