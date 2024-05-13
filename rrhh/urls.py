from django.urls import path
from . import views
from .views import *

app_name="rrhh"

urlpatterns = [
   
    path('reportes_rrhh/', views.app_rrhh, name='rrhh_panel'),
]