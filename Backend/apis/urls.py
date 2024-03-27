from django.urls import path,include
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'solicitud_transplantes', views.solicitud_transplantesViewSet)
router.register(r'organos', views.organosViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

