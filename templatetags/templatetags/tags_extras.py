from django import template
from django.contrib.auth.models import User
from usuarios.models import datosusuario


register = template.Library()


@register.filter('logo')
def logo(identificacion):

    try:
        usuario = datosusuario.objects.get(identificacion = identificacion)
        return usuario.imagenlogo.url


    except:
        return "{% static 'img/avatar.png' %}"