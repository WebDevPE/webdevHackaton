from django.db import models

# Create your models here.
class Hoja(models.Model):
    idhoja=models.IntegerField(primary_key=True)
    Titulo=models.CharField(max_length=20)
    Fecha=models.DateTimeField(auto_now_add=True)
    Ideas=models.CharField(max_length=600)
    Tema=models.CharField(max_length=700)
    Resumen=models.CharField(max_length=600)
    
    
    def __str__(self):
        return self.Titulo