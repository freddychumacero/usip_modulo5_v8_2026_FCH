from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CuentaBancariaViewSet,
    CategoriaMovimientoViewSet,
    IngresoViewSet,
    EgresoViewSet,
    ResumenTesoreriaAPIView,
)

router = DefaultRouter()
router.register(r'cuentas', CuentaBancariaViewSet)
router.register(r'categorias', CategoriaMovimientoViewSet)
router.register(r'ingresos', IngresoViewSet)
router.register(r'egresos', EgresoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('resumen/', ResumenTesoreriaAPIView.as_view(), name='resumen-tesoreria'),
]
