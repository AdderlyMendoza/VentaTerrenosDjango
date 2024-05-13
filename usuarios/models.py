from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyectos

# Create your models here.
class datosusuario(models.Model):

    class estados(models.TextChoices):

        ACTIVO = "ACTIVO"
        NO = "NO ACTIVO"

    class check_tuto(models.TextChoices):

        SI = "SI"
        NO = "NO"

    user=models.OneToOneField(User, blank=True,null=True,on_delete=models.SET_NULL)
    identificacion = models.CharField(max_length=200, verbose_name="Identificacion")
    nombre = models.CharField(max_length=200, verbose_name="Nombre, Apellido", blank=True, null=True,)
    imagen = models.CharField(max_length=200, verbose_name="Imagen", blank=True, null=True, editable=False)
    imagenlogo = models.ImageField(verbose_name="Imagen", blank=True, null=True)
    area = models.CharField(max_length=200, verbose_name="Area", blank=True, null=True)
    cargo = models.CharField(max_length=200, verbose_name="Cargo", blank=True, null=True)
    email = models.CharField(max_length=200, verbose_name="Email", blank=True, null=True)
    estado = models.CharField(choices=estados.choices, default=estados.ACTIVO, max_length=20, verbose_name="Estado")
    fecha_ingreso = models.DateField(verbose_name = "Fecha de ingreso", blank=True, null=True)
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de nacimiento", blank=True, null=True)
    Telefono = models.CharField(max_length=200, verbose_name="Telefono", blank=True, null=True)
    Comentarios = models.TextField(verbose_name="Comentarios", blank=True, null=True)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name = "Proyecto que sigue", blank=True, null=True)
    tutorial = models.CharField(choices=check_tuto.choices, default=check_tuto.NO, max_length=20, verbose_name="Tutorial", blank=True, null=True)

    class Meta:
        verbose_name="Dato de usuario"
        verbose_name_plural="Datos de los usuarios"

    def __str__(self):
        return self.identificacion
    

class ActividadesUsuarios(models.Model):

    usuario = models.ForeignKey(datosusuario, on_delete=models.CASCADE, verbose_name="Usuario")
    categoria = models.CharField(max_length=30, verbose_name="Categoria")
    accion = models.CharField(max_length=50, verbose_name="Acción")
    momento = models.DateTimeField(verbose_name= "Fecha")

    class Meta:
        verbose_name="Actividad"
        verbose_name_plural="Actividades"

    def __str__(self):
        return f'{self.usuario.identificacion} - {self.categoria} - {self.accion}'
        