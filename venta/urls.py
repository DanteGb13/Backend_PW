from django.urls import path
from . import views
from .views import menu_view

app_name = 'tienda'



urlpatterns = [
    path(' ', views.index, name='menu'),
    path('venta/', include('venta.urls')), 
    
    
    ]