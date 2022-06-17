from django.db import models
from pyparsing import makeXMLTags


# Create your models here.
class Familia(models.model):
    nombre=models.CharField(max_length=10)
    edad=models.IntegerField()
    fecha=models.DateField()
    def __str__(self):
       texto="{0} {{1}}"
       return texto.formato(self.nombre,self.edad,self.fecha)


#class madre(models.Model):
    #nombre=models.CharField(max_length=20)
    #edad =models.IntegerField()
    #fecha=models.DateField()

#class padre(models.Model):
 #    nombre=models.CharField(max_length=20)
  #   edad=models.IntegerField()
   #  fecha=models.DateField()

#class hermano(models.Model):
 #   nombre=models.CharField(max_length=20)
  #  edad=models.IntegerField()
   # fecha=models.DateField()



  
