from rest_framework import viewsets
from .models import solicitud_transplantes, organos
from .serializer import solicitud_transplantesSerializer, organosSerializer
from rest_framework.response import Response
from rest_framework import status

class solicitud_transplantesViewSet(viewsets.ModelViewSet):
    queryset = solicitud_transplantes.objects.all()
    serializer_class = solicitud_transplantesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
class organosViewSet(viewsets.ModelViewSet):
	queryset = organos.objects.all()
	serializer_class = organosSerializer
	