# Generated by Django 5.0.4 on 2024-05-13 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('ACTIVO', 'Activo'), ('DISPONIBLE', 'Disponible')], default='ACTIVO', max_length=20, verbose_name='Estado')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('ACTIVO', 'Activo'), ('CANCELADO', 'Cancelado')], default='ACTIVO', max_length=20, verbose_name='Estado')),
                ('nombres', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('monto_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento_faltas', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora_llegada', models.TimeField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
            ],
        ),
    ]
