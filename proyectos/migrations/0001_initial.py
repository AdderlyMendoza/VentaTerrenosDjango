# Generated by Django 5.0.4 on 2024-05-13 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubigeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('ACTIVO', 'Activo'), ('VENDIDO', 'Vendido'), ('PENDIENTE', 'Pendiente')], default='ACTIVO', max_length=30)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del proyecto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('google_maps', models.CharField(blank=True, max_length=400, null=True, verbose_name='Google Maps')),
                ('tipo', models.CharField(max_length=50)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('observacion', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubigeo.distrito', verbose_name='Ubicacion')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Sub_Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('VENDIDO', 'Vendido'), ('DISPONIBLE', 'Disponible'), ('SEPARADO', 'Separado')], default='DISPONIBLE', max_length=20, verbose_name='Estado')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('m2', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
                ('plano', models.FileField(blank=True, null=True, upload_to='plano/', verbose_name='Plano')),
                ('observacion', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyectos')),
            ],
            options={
                'verbose_name': 'Sub_Proyecto',
                'verbose_name_plural': 'Sub_Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen')),
                ('sub_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='proyectos.sub_proyecto')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
    ]