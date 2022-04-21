from django.db import models

class usuario(models.Model):
    def toJson(self):   
        a = {'id':self.id, 'progresoPorcentual':self.progresoPorcentual, 'minutosJugados':self.minutosJugados, 'usuario':self.usuario} #TODOS}
        return a
        
    id = models.AutoField(primary_key=True)
    progresoPorcentual = models.IntegerField(null=True)
    minutosJugados = models.IntegerField(null=True)
    usuario = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200,null=True)

