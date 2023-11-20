from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import AdministradorViewSet, OrganizadorViewSet, AtletaViewSet, EstadoViewSet, CidadeViewSet, ContatoOrganizadorViewSet, ContatoAtletaViewSet, CorridaViewSet

router = routers.DefaultRouter()
router.register(r'administradores', AdministradorViewSet)
router.register(r'organizadores', OrganizadorViewSet)
router.register(r'atletas', AtletaViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'contato_organizadores', ContatoOrganizadorViewSet)
router.register(r'contato_atletas', ContatoAtletaViewSet)
router.register(r'corridas', CorridaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
