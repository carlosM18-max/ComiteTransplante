from rest_framework import viewsets
from .models import solicitud_transplantes, organos
from .serializer import solicitud_transplantesSerializer, organosSerializer

class solicitud_transplantesViewSet(viewsets.ModelViewSet):
	queryset = solicitud_transplantes.objects.all()
	serializer_class = solicitud_transplantesSerializer
	
class organosViewSet(viewsets.ModelViewSet):
	queryset = organos.objects.all()
	serializer_class = organosSerializer
	