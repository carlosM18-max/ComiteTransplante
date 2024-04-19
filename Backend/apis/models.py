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
    titulo = models.CharField(max_length=45, null=True)
    nombre = models.CharField(max_length=80)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80, null=True)
    curp = models.CharField(max_length=18, unique=True, null=True)
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
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(null=True)

    class Meta:
        db_table = 'personas'

    def  __str__(self):
        return str(self.ID)

class pacientes(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    nss = models.CharField(max_length=15, null=True)
    tipo_seguro = models.CharField(max_length=50, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_ultima_cita = models.DateTimeField()
    estatus_medico = models.CharField(max_length=100, default='Normal', null=True)
    class estatusVidaOpciones(models.TextChoices):
        Vivo = 'Vivo'
        Finado = 'Finado'
        Coma = 'Coma'
        Vegetativo = 'Vegetativo'
    estatus_vida = models.CharField(max_length=50, choices=estatusVidaOpciones.choices, default='Vivo')
    estatus = models.BooleanField(null=True)

    class Meta:
        db_table = 'pacientes'

    def __str__(self):
        return str(self.persona_ID)

class personal_medico(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    especialidad = models.CharField(max_length=50, null=True)
    class tipoOpciones(models.TextChoices):
        Medico = 'Médico'
        Enfermero = 'Enfermero'
        Administrativo = 'Administrativo'
        Directivo = 'Directivo'
        Apoyo = 'Apoyo'
        Residente = 'Residente'
        Interno = 'Interno'
    tipo = models.CharField(max_length=50, choices=tipoOpciones.choices)
    cedula_profesional = models.CharField(max_length=50, unique=True, null=True)
    departamento_ID = models.PositiveIntegerField()
    class estatusOpciones(models.TextChoices):
        Activo = 'Activo'
        Inactivo = 'Inactivo'
        Jubilado = 'Jubilado'
        Permiso = 'Permiso'
    
    estatus = models.CharField(max_length=50, choices=estatusOpciones.choices)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    fecha_termino_contrato = models.DateTimeField(null=True)

    class Meta:
        db_table = 'personal_medico'

    def __str__(self):
        return str(self.persona_ID)

class organos(models.Model):    
    ID = UnsignedIntAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    aparato_sistema = models.CharField(max_length=50)
    descripcion = models.TextField()
    detalle_organo_ID = models.PositiveIntegerField()
    estatus = models.BooleanField()

    class Meta:
        db_table = 'organos'

    def __str__(self):
        return str(self.ID)

class solicitud_transplantes(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    paciente_ID = UnsignedForeignKey(pacientes, related_name='fk_paciente_ID', on_delete=models.CASCADE, db_column='paciente_ID')
    medico_ID = UnsignedForeignKey(personal_medico, related_name='fk_medico_ID', on_delete=models.CASCADE, db_column='medico_ID')
    organo_ID = UnsignedForeignKey(organos, related_name='fk_organo_ID', on_delete=models.CASCADE, db_column='organo_ID')
 
    class prioridadOpciones(models.TextChoices):
       Urgente = 'Urgente' 
       Alta = 'Alta'
       Moderada = 'Moderada'
    prioridad = models.CharField( max_length = 50, choices=prioridadOpciones.choices)
 
    fecha_solicitud = models.DateTimeField()
    dias_espera = models.IntegerField(null=True)
 
    class estatusOpciones(models.TextChoices):
       Transplante_exitoso = 'Transplante exitoso'
       Recuperacion = 'Recuperacion'
       Pendiente = 'Pendiente'
    estatus = models.CharField(default='Pendiente', max_length = 50, choices=estatusOpciones.choices, null=True) 
    estatus_aprobacion = models.BooleanField(default=False, null=True)
    
    class Meta:
        db_table = 'solicitud_transplantes'

    def __str__(self):
        return str(self.ID)