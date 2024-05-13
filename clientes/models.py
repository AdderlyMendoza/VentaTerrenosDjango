from django.db import models
from datetime import timedelta
from django.db.models.signals import pre_save, post_save
from proyectos.models import *
from django.dispatch import receiver

class Cliente(models.Model):

    nombres = models.CharField(max_length=100)
    ap_paterno  = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    documento = models.IntegerField()
    celular = models.IntegerField()
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.nombres


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, related_name='ventas', blank=True, null=True)
    subproyecto = models.ForeignKey(Sub_Proyecto, on_delete=models.CASCADE, related_name='ventas')
    precio_venta = models.FloatField()
    forma_pago = models.CharField(max_length=20, choices=[('contado', 'Contado'), ('cuotas', 'Cuotas')])
    cuotas = models.IntegerField(verbose_name="Cuotas", default=1, null=False)
    fecha_creacion =models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.subproyecto.estado = 'SEPARADO'
        self.subproyecto.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Venta")
        verbose_name_plural = ("Ventas")

    def __str__(self):
        return f"Venta de {self.subproyecto.nombre} del proyecto {self.proyecto.nombre} a {self.cliente.nombres}"
    
@receiver(pre_save, sender=Venta)
def actualizar_precio_venta(sender, instance, **kwargs):
   
    instance.precio_venta = instance.subproyecto.precio_venta
    instance.proyecto = instance.subproyecto.proyecto

@receiver(pre_save, sender=Venta)
def verificar_subproyecto(sender, instance, **kwargs):
    if instance.subproyecto.ventas.exists():
        raise ValueError('Este subproyecto ya está asociado a una venta')


class Cuota(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado')
    )

    venta = models.ForeignKey('clientes.Venta', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    estado_pago = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Cuota de {self.venta} - Monto: {self.monto} - Fecha de Vencimiento: {self.fecha_vencimiento}"

@receiver(post_save, sender='clientes.Venta')
def generar_cuotas(sender, instance, created, **kwargs):
    if created:

        precio_venta = instance.precio_venta
        cantidad_cuotas = instance.cuotas


        monto_cuota = min(instance.precio_venta / cantidad_cuotas, instance.precio_venta)

        fecha_vencimiento = instance.fecha_creacion.date() + timedelta(days=30)  

        for _ in range(cantidad_cuotas):
            Cuota.objects.create(
                venta=instance,
                monto=monto_cuota,
                fecha_vencimiento=fecha_vencimiento
            )
            fecha_vencimiento += timedelta(days=30)  


class Cobro(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    

    def __str__(self):
        return f"Cobro de {self.monto} para la venta {self.venta}"
    
