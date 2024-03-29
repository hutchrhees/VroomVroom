# Generated by Django 4.0.3 on 2022-12-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_alter_technicianvo_employee_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceappointment',
            name='automobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='automobile', to='service_rest.automobilevo'),
        ),
        migrations.AlterField(
            model_name='serviceappointment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='service_rest.customervo'),
        ),
        migrations.AlterField(
            model_name='serviceappointment',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technician', to='service_rest.technicianvo'),
        ),
    ]
