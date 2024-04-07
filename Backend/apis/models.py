from django.db import models
from django.utils import timezone

class UnsignedIntAutoField(models.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.settings_dict['ENGINE']:
            return 'int UNSIGNED AUTO_INCREMENT'
        return 'int'

class UnsignedForeignKey(models.ForeignKey):
    def db_type(self, connection):
        if 'mysql' in connection.settings_dict['ENGINE']:
            return 'int UNSIGNED'
        return 'int'

class personas(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    titulo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=80)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80)
    curp = models.CharField(max_length=18)
    class generoOpciones(models.TextChoices):
        M = 'M' 
        F = 'F'
        NB = 'N/B'
    genero = models.CharField(max_length=50, choices=generoOpciones.choices)
    class grupoSanguineoOpciones(models.TextChoices):
        A = 'A'
        B = 'B'
        AB = 'AB'
        O = 'O'
    grupo_sanguineo = models.CharField(max_length=50, choices=grupoSanguineoOpciones.choices)
    class tipoSanguineoOpciones(models.TextChoices):
        Positivo = '+' 
        Negativo = '-'
    tipo_sanguineo = models.CharField(max_length=50, choices=tipoSanguineoOpciones.choices)
    fecha_nacimiento = models.DateField()
    estatus = models.BooleanField(default=True)
    fecha_nacimiento = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField()

    def  __str__(self):
        return self.ID

class pacientes(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    nss = models.CharField(max_length=15)
    tipo_seguro = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_ultima_cita = models.DateTimeField()
    estatus_medico = models.CharField(max_length=100, default='Normal')
    class estatusVidaOpciones(models.TextChoices):
        Vivo = 'Vivo'
        Finado = 'Finado'
        Coma = 'Coma'
        Vegetativo = 'Vegetativo'
    estatus_vida = models.CharField(max_length=50, choices=estatusVidaOpciones.choices)
    estatus = models.BooleanField()

    def __str__(self):
        return self.persona_ID

class personal_medico(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    especialidad = models.CharField(max_length=50)
    class tipoOpciones(models.TextChoices):
        Medico = 'Médico'
        Enfermero = 'Enfermero'
        Administrativo = 'Administrativo'
        Directivo = 'Directivo'
        Apoyo = 'Apoyo'
        Residente = 'Residente'
        Interno = 'Interno'
    tipo = models.CharField(max_length=50, choices=tipoOpciones.choices)
    cedula_profesional = models.CharField(max_length=50)
    departamento_ID = models.PositiveIntegerField()
    class estatusOpciones(models.TextChoices):
        Activo = 'Activo'
        Inactivo = 'Inactivo'
        Jubilado = 'Jubilado'
        Permiso = 'Permiso'
    
    estatus = models.CharField(max_length=50, choices=estatusOpciones.choices)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    fecha_termino_contrato = models.DateTimeField()

    def __str__(self):
        return self.persona_ID

class organos(models.Model):    
    ID = UnsignedIntAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    aparato_sistema = models.CharField(max_length=50)
    # descripcion = models.TextField()
    detalle_organo_ID = models.PositiveIntegerField()
    estatus = models.BooleanField()

    def __str__(self):
        return self.ID

class solicitud_transplantes(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    paciente_ID = UnsignedForeignKey(pacientes, on_delete=models.CASCADE, db_column='paciente_ID')
    medico_ID = UnsignedForeignKey(personal_medico, on_delete=models.CASCADE, db_column='medico_ID')
    organo_ID = UnsignedForeignKey(organos, on_delete=models.CASCADE, db_column='organo_ID')
 
    class prioridadOpciones(models.TextChoices):
       Urgente = 'Urgente' 
       Alta = 'Alta'
       Moderada = 'Moderada'
    prioridad = models.CharField( max_length = 50, choices=prioridadOpciones.choices)
 
    fecha_solicitud = models.DateTimeField()
    dias_espera = models.IntegerField()
 
    class estatusOpciones(models.TextChoices):
       Transplante_exitoso = 'Transplante exitoso'
       Recuperacion = 'Recuperacion'
       Pendiente = 'Pendiente'
    estatus = models.CharField(max_length = 50, choices=estatusOpciones.choices) 
    estatus_aprobacion = models.BooleanField(default=False)
    
    def __str__(self):
        return self.ID