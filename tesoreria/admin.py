from django.contrib import admin
from .models import CuentaBancaria, CategoriaMovimiento, Ingreso, Egreso


@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'banco', 'numero_cuenta', 'moneda', 'saldo_inicial', 'activa')
    list_filter = ('banco', 'moneda', 'activa')
    search_fields = ('nombre', 'banco', 'numero_cuenta')


@admin.register(CategoriaMovimiento)
class CategoriaMovimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nombre',)


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'fecha', 'cuenta', 'categoria')
    list_filter = ('cuenta', 'categoria', 'fecha')
    search_fields = ('descripcion', 'referencia')
    date_hierarchy = 'fecha'


@admin.register(Egreso)
class EgresoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'fecha', 'cuenta', 'categoria')
    list_filter = ('cuenta', 'categoria', 'fecha')
    search_fields = ('descripcion', 'referencia')
    date_hierarchy = 'fecha'
