from django.contrib import admin
from .models import solicitud_transplantes, organos

# Register your models here.
admin.site.register(solicitud_transplantes)
admin.site.register(organos)