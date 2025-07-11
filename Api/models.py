from django.db import models

class Productos(models.Model):
    Codprodu=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=30)
    Precio=models.IntegerField()
    Stock=models.IntegerField()
    Desc=models.TextField()
    Imagen=models.ImageField(upload_to="productos",null=True)
    def __int__(self):
        self.Codprodu
# Create your models here.
