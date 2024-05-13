from django.urls import path
from . import views
from .views import *

app_name="socios"

urlpatterns = [
   
    path('socios_panel/', views.app_socios, name='socios_panel'),
]
