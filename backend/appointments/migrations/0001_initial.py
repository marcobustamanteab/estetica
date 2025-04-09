# Generated by Django 4.2.10 on 2025-03-25 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('start_time', models.TimeField(verbose_name='Hora de inicio')),
                ('end_time', models.TimeField(verbose_name='Hora de fin')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('confirmed', 'Confirmada'), ('cancelled', 'Cancelada'), ('completed', 'Completada')], default='pending', max_length=20, verbose_name='Estado')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='clients.client', verbose_name='Cliente')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL, verbose_name='Empleado')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='services.service', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ['date', 'start_time'],
            },
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(fields=('employee', 'date', 'start_time'), name='unique_appointment'),
        ),
    ]
