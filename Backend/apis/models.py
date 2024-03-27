from django.db import models

class UnsignedIntAutoField(models.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.settings_dict['ENGINE']:
            return 'int UNSIGNED AUTO_INCREMENT'
        return 'int'

# Create your models here.
class solicitud_transplantes(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    paciente_ID = models.IntegerField()
    medico_ID = models.IntegerField()
    organo_ID = models.IntegerField()
 
    class prioridadClass(models.TextChoices):
       Urgente = 'Urgente' 
       Alta = 'Alta'
       Moderada = 'Moderada'
    prioridad = models.CharField( max_length = 255, choices=prioridadClass.choices)
 
    fecha_solicitud = models.DateTimeField()
    dias_espera = models.IntegerField()
 
    class estatusClass(models.TextChoices):
       Transplante_exitoso = 'Transplante exitoso'
       Recuperacion = 'Recuperacion'
       Pendiente = 'Pendiente'
    estatus = models.CharField(max_length = 255, choices=estatusClass.choices) 
    estatus_aprobacion = models.BooleanField(default=False)
    
    def __str__(self):
        return self.ID

class organos(models.Model):    
   ID = UnsignedIntAutoField(primary_key=True)
   nombre = models.CharField(max_length=45)
   aparato_sistema = models.CharField(max_length=50)
   descripcion = models.TextField()
   detalle_organo_ID = models.PositiveIntegerField()
   estatus = models.BooleanField()

   def __str__(self):
        return self.ID