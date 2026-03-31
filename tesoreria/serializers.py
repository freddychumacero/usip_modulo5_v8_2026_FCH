from rest_framework import serializers
from .models import CuentaBancaria, CategoriaMovimiento, Ingreso, Egreso


class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'


class CategoriaMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMovimiento
        fields = '__all__'


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'


class EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egreso
        fields = '__all__'
