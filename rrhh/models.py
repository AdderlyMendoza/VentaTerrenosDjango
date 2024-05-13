from django.db import models
from datetime import datetime, timedelta


class Cargo(models.Model):
    class estado(models.TextChoices):

            ACTIVO = "ACTIVO"
            DISPONIBLE = "DISPONIBLE"

    estado = models.CharField(choices=estado.choices, default="ACTIVO", max_length=20, verbose_name="Estado")
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    class estados(models.TextChoices):

            ACTIVO = "ACTIVO"
            CANCELADO = "CANCELADO"
           

    estado = models.CharField(choices=estados.choices, default="ACTIVO", max_length=20, verbose_name="Estado")
    nombres = models.CharField(max_length=200)
    dni = models.CharField(max_length=10, unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    descuento_faltas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombres


class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    hora_llegada = models.TimeField()

    def __str__(self):
        return f"Asistencia de {self.empleado} el {self.fecha}"

    def calcular_descuento(self):
        hora_llegada_correcta = self.empleado.cargo.hora_llegada
        hora_tolerancia = hora_llegada_correcta + timedelta(minutes=15)  # Suponiendo una tolerancia de 15 minutos
        if self.hora_llegada > hora_tolerancia:
            # Calcula el tiempo de retraso y aplica un descuento
            tiempo_retraso = self.hora_llegada - hora_llegada_correcta
            descuento = tiempo_retraso.total_seconds() / 3600 * 5  # TARIFA_DESCUENTO es el valor a descontar por hora de retraso
            return descuento
        else:
            return 0