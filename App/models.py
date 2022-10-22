from datetime import timezone
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.timezone import now
from django.utils import timezone



class Almacen(models.Model):
    # Area de almacenamiento de piezas
    nombre_entrega=models.CharField(max_length=50)
    nombre_jefeLinea=models.CharField(max_length=50)
    
    piezasAutomotriz = models.IntegerField()    
    piezasMicrotec = models.IntegerField()
    #TERMINADAS
    productosAutomotrizTerminadas = models.IntegerField()    
    productosAutomotrizTerminadas = models.IntegerField() 
    #   
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    
   
