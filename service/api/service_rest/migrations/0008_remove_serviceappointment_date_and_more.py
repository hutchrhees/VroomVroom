# Generated by Django 4.0.3 on 2022-12-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0007_remove_automobilevo_import_href'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceappointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='serviceappointment',
            name='time',
        ),
        migrations.AddField(
            model_name='serviceappointment',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
