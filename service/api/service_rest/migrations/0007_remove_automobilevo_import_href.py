# Generated by Django 4.0.3 on 2022-12-08 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0006_serviceappointment_automobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobilevo',
            name='import_href',
        ),
    ]