from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar_sistema, name='login'),
    path('panel/', views.panel_principal, name='panel_principal'),
    path('salir/', views.cerrar_sesion_usuario, name='logout'),
    
    path('registros/', views.lista_clientes, name='lista_clientes'),
    path('registros/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('registros/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('registros/borrar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
]