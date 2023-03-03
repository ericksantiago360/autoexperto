from django.db import models

class datosdelauto(models.Model):
    id= models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=200, verbose_name='titulo') 
    imagen = models.ImageField(upload_to='imagenes/',verbose_name= 'imagen', null=True)
    imagen2 = models.ImageField(upload_to='imagenes/',verbose_name= 'imagen2', null=True)
    imagen3 = models.ImageField(upload_to='imagenes/',verbose_name= 'imagen3', null=True)
    imagen4 = models.ImageField(upload_to='imagenes/',verbose_name= 'imagen4', null=True)
    marcadelauto = models.CharField(max_length=200, verbose_name= 'marcadelauto', null=True )
    modelo = models.CharField(max_length=200, verbose_name='modelo', null=True)
    precio = models.CharField(max_length=200, verbose_name='precio',null= True) 
    descripcion = models.TextField( verbose_name= 'Descripcion',null = True)  
    kilometraje= models.CharField(max_length=200, verbose_name='kilometraje', null=True)
    estadodelvehiculo = models.CharField(max_length=200, verbose_name='estadodelvehiculo', null=True)
    factura = models.CharField(max_length=200, verbose_name='factura', null=True)
    numerodedueno = models.CharField(max_length=200, verbose_name='numerodedueno', null=True)
          
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
        
    
    