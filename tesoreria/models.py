from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validar_monto_positivo(value):
    if value <= 0:
        raise ValidationError('El monto debe ser mayor a cero.')


def validar_fecha_no_futura(value):
    if value > timezone.now().date():
        raise ValidationError('La fecha no puede ser futura.')


class CuentaBancaria(models.Model):
    MONEDA_CHOICES = [
        ('BOB', 'Bolivianos'),
        ('USD', 'Dólares'),
        ('EUR', 'Euros'),
    ]

    nombre = models.CharField(max_length=150)
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=50, unique=True)
    moneda = models.CharField(max_length=3, choices=MONEDA_CHOICES, default='BOB')
    saldo_inicial = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    activa = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} - {self.banco} ({self.moneda})'

    class Meta:
        verbose_name = 'Cuenta Bancaria'
        verbose_name_plural = 'Cuentas Bancarias'


class CategoriaMovimiento(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre} ({self.get_tipo_display()})'

    class Meta:
        verbose_name = 'Categoría de Movimiento'
        verbose_name_plural = 'Categorías de Movimientos'


class Ingreso(models.Model):
    cuenta = models.ForeignKey(
        CuentaBancaria, on_delete=models.PROTECT, related_name='ingresos'
    )
    categoria = models.ForeignKey(
        CategoriaMovimiento, on_delete=models.PROTECT, related_name='ingresos',
        limit_choices_to={'tipo': 'ingreso'}
    )
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(
        max_digits=14, decimal_places=2, validators=[validar_monto_positivo]
    )
    fecha = models.DateField(validators=[validar_fecha_no_futura])
    referencia = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Ingreso S/{self.monto} - {self.descripcion} ({self.fecha})'

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['-fecha']


class Egreso(models.Model):
    cuenta = models.ForeignKey(
        CuentaBancaria, on_delete=models.PROTECT, related_name='egresos'
    )
    categoria = models.ForeignKey(
        CategoriaMovimiento, on_delete=models.PROTECT, related_name='egresos',
        limit_choices_to={'tipo': 'egreso'}
    )
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(
        max_digits=14, decimal_places=2, validators=[validar_monto_positivo]
    )
    fecha = models.DateField(validators=[validar_fecha_no_futura])
    referencia = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Egreso S/{self.monto} - {self.descripcion} ({self.fecha})'

    class Meta:
        verbose_name = 'Egreso'
        verbose_name_plural = 'Egresos'
        ordering = ['-fecha']
