# Generated by Django 3.1.7 on 2021-04-24 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20210424_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2021, 4, 24, 13, 44, 27, 995835)),
        ),
    ]
