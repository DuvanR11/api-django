from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    catNombre = models.CharField(max_length=50)
    catFoto = models.FileField(upload_to='categoria/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.catNombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    proCodigo = models.IntegerField(unique=True, null=False)
    proNombre = models.CharField(max_length=255, null=False)
    proPrecio = models.IntegerField(null=False)
    proCateforia = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proFoto = models.FileField(upload_to='productos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.proNombre
    