from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CuentaBancaria, CategoriaMovimiento, Ingreso, Egreso
from .serializers import (
    CuentaBancariaSerializer,
    CategoriaMovimientoSerializer,
    IngresoSerializer,
    EgresoSerializer,
)


class CuentaBancariaViewSet(viewsets.ModelViewSet):
    queryset = CuentaBancaria.objects.all()
    serializer_class = CuentaBancariaSerializer


class CategoriaMovimientoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaMovimiento.objects.all()
    serializer_class = CategoriaMovimientoSerializer


class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.select_related('cuenta', 'categoria').all()
    serializer_class = IngresoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        cuenta_id = self.request.query_params.get('cuenta')
        if cuenta_id:
            qs = qs.filter(cuenta_id=cuenta_id)
        return qs


class EgresoViewSet(viewsets.ModelViewSet):
    queryset = Egreso.objects.select_related('cuenta', 'categoria').all()
    serializer_class = EgresoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        cuenta_id = self.request.query_params.get('cuenta')
        if cuenta_id:
            qs = qs.filter(cuenta_id=cuenta_id)
        return qs


class ResumenTesoreriaAPIView(APIView):
    """
    Custom API: devuelve el resumen de tesorería por cuenta bancaria.
    GET /api/tesoreria/resumen/
    """

    def get(self, _request):
        cuentas = CuentaBancaria.objects.filter(activa=True)
        resumen = []

        for cuenta in cuentas:
            total_ingresos = (
                Ingreso.objects.filter(cuenta=cuenta)
                .aggregate(total=Sum('monto'))['total'] or 0
            )
            total_egresos = (
                Egreso.objects.filter(cuenta=cuenta)
                .aggregate(total=Sum('monto'))['total'] or 0
            )
            saldo_actual = cuenta.saldo_inicial + total_ingresos - total_egresos

            resumen.append({
                'cuenta_id': cuenta.id,
                'nombre': cuenta.nombre,
                'banco': cuenta.banco,
                'moneda': cuenta.moneda,
                'saldo_inicial': cuenta.saldo_inicial,
                'total_ingresos': total_ingresos,
                'total_egresos': total_egresos,
                'saldo_actual': saldo_actual,
            })

        totales_globales = {
            'total_ingresos_global': sum(r['total_ingresos'] for r in resumen),
            'total_egresos_global': sum(r['total_egresos'] for r in resumen),
            'saldo_neto_global': sum(r['saldo_actual'] for r in resumen),
        }

        return Response(
            {'cuentas': resumen, 'totales': totales_globales},
            status=status.HTTP_200_OK,
        )
