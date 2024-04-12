from rest_framework import viewsets, status
from .models import personas, pacientes, personal_medico, organos, solicitud_transplantes
from .serializer import personasSerializer, pacientesSerializer, personal_medicoSerializer, organosSerializer, solicitud_transplantesSerializer
from rest_framework.response import Response
	
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

	def create(self, request, *args, **kwargs):
		try:
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			self.perform_create(serializer)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)