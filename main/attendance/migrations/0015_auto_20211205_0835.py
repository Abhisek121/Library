# Generated by Django 3.2.9 on 2021-12-05 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_auto_20211205_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='time_in',
        ),
        migrations.RemoveField(
            model_name='record',
            name='time_out',
        ),
    ]
