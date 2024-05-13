from django.urls import path
from . import views
from .views import *

app_name="usuarios"

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.login, name="login"),
    path('home/', HomeView.as_view(), name="home"),
    path('logout', views.logout, name = 'Logout'),

    
    
    # Your URL patterns here
]