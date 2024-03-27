from rest_framework import serializers
from .models import solicitud_transplantes, organos

class solicitud_transplantesSerializer(serializers.ModelSerializer):
	class Meta:
		model = solicitud_transplantes
		fields = '__all__'
		
class organosSerializer(serializers.ModelSerializer):
	class Meta:
		model = organos
		fields = '__all__'
