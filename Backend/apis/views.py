from rest_framework import viewsets
from .models import personas, pacientes, personal_medico, organos, solicitud_transplantes
from .serializer import personasSerializer, pacientesSerializer, personal_medicoSerializer, organosSerializer, solicitud_transplantesSerializer

	
class personasViewSet(viewsets.ModelViewSet):
	queryset = personas.objects.all()
	serializer_class = personasSerializer
	
class pacientesViewSet(viewsets.ModelViewSet):
	queryset = pacientes.objects.all()
	serializer_class = pacientesSerializer
	
class personal_medicoViewSet(viewsets.ModelViewSet):
	queryset = personal_medico.objects.all()
	serializer_class = personal_medicoSerializer
	
class organosViewSet(viewsets.ModelViewSet):
	queryset = organos.objects.all()
	serializer_class = organosSerializer
	
class solicitud_transplantesViewSet(viewsets.ModelViewSet):
	queryset = solicitud_transplantes.objects.all()
	serializer_class = solicitud_transplantesSerializer