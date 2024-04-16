from rest_framework import serializers
from .models import personas, pacientes, personal_medico, organos, solicitud_transplantes



class personasSerializer(serializers.ModelSerializer):
	class Meta:
		model = personas
		fields = '__all__'

class pacientesSerializer(serializers.ModelSerializer):
	class Meta:
		model = pacientes
		fields = '__all__'

class personal_medicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = personal_medico
		fields = '__all__'

class organosSerializer(serializers.ModelSerializer):
	class Meta:
		model = organos
		fields = '__all__'

class solicitud_transplantesSerializer(serializers.ModelSerializer):
	class Meta:
		model = solicitud_transplantes
		fields = '__all__'