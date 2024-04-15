from django.urls import path,include
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'personas', views.personasViewSet)
router.register(r'pacientes', views.pacientesViewSet)
router.register(r'personal_medico', views.personal_medicoViewSet)
router.register(r'organos', views.organosViewSet)
router.register(r'solicitud_transplantes', views.solicitud_transplantesViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

