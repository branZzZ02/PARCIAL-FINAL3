from django.db import models

from django.db import models

class Cliente(models.Model):
    # CAMBIO DE NOMBRES PARA DESPISTAR
    documento = models.CharField(max_length=20, unique=True, verbose_name="Cédula")
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(verbose_name="E-mail")
    celular = models.CharField(max_length=15)
    ubicacion = models.TextField(verbose_name="Dirección")
    
    # Fecha de registro automática
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"