# Generated by Django 3.2.9 on 2021-12-05 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_auto_20211205_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='issuedDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='record',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2021, 12, 5, 8, 13, 35, 504794)),
        ),
    ]
