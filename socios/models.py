from django.db import models
from proyectos.models import *
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.



class Socio(models.Model):
    estado = models.BooleanField(max_length=20, choices=(('activo', 'Activo'), ('no activo', 'No Activo')), default='activo')
    documento = models.IntegerField(max_length=9)
    nombre = models.CharField(max_length=200)
    ap_paterno =models.CharField(max_length=50)
    ap_Materno =models.CharField(max_length=50)
    celular = models.IntegerField()
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

class Inversion(models.Model):
    tipo = models.CharField(max_length=20, choices=(('inversionista', 'Inversionista'), ('socio', 'Socio')), default='inversionista')
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    proyectos = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    cantidad_invertida = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.socio.nombre} - {self.proyectos.nombre}"

class Pagos(models.Model):
    inversion = models.ForeignKey(Inversion, on_delete=models.CASCADE)
    cantidad_invertida = models.FloatField()
    monto = models.IntegerField()
    saldo = models.IntegerField()
    fecha_pago =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Pago")
        verbose_name_plural = ("Pagos")

    def __str__(self):
        return f"Pago de {self.inversion.socio.nombre} en {self.fecha_pago}"

@receiver(pre_save, sender=Pagos)
def calcular_intereses(sender, instance, **kwargs):
    proyecto = instance.inversion.proyectos
    tasa_interes = proyecto.tasa_interes_anual
   
    intereses = instance.cantidad_invertida * (tasa_interes / 100)

    instance.monto = instance.cantidad_invertida + intereses