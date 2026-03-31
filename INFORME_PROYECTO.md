# Informe de Proyecto — Módulo V: Django

**Alumno:** Freddy Einard Chumacero Cors  
**Proyecto:** Sistema de Gestión de Tesorería  
**Fecha:** 30 de marzo de 2026

---

## 1. Descripción del Proyecto

Se desarrolló un **Sistema de Gestión de Tesorería** para una pequeña empresa. El sistema permite administrar cuentas bancarias, registrar ingresos y egresos categorizados, y obtener un resumen financiero en tiempo real con saldos actualizados por cuenta.

---

## 2. Cumplimiento de Requerimientos

### ✅ Proyecto Django con al menos una Aplicación

El proyecto se llama **`ecoapp`** y contiene la aplicación **`tesoreria`**.

```
usip_modulo5_v8_2026_FCH/
├── ecoapp/          ← Proyecto Django (settings, urls, wsgi, asgi)
├── tesoreria/       ← Aplicación principal
├── manage.py
└── requirements.txt
```

---

### ✅ Al menos 4 Models

Definidos en [tesoreria/models.py](tesoreria/models.py):

| # | Modelo | Descripción |
|---|--------|-------------|
| 1 | `CuentaBancaria` | Registra cuentas bancarias con banco, número, moneda y saldo inicial |
| 2 | `CategoriaMovimiento` | Clasifica movimientos como ingreso o egreso |
| 3 | `Ingreso` | Registra entradas de dinero vinculadas a una cuenta y categoría |
| 4 | `Egreso` | Registra salidas de dinero vinculadas a una cuenta y categoría |

---

### ✅ Al menos 2 Validaciones Personalizadas

Implementadas como funciones de validación en [tesoreria/models.py](tesoreria/models.py):

**Validación 1 — `validar_monto_positivo`**
```python
def validar_monto_positivo(value):
    if value <= 0:
        raise ValidationError('El monto debe ser mayor a cero.')
```
Aplicada en los campos `monto` de `Ingreso` y `Egreso`.

**Validación 2 — `validar_fecha_no_futura`**
```python
def validar_fecha_no_futura(value):
    if value > timezone.now().date():
        raise ValidationError('La fecha no puede ser futura.')
```
Aplicada en los campos `fecha` de `Ingreso` y `Egreso`.

---

### ✅ Al menos 2 Models registrados en el Administrador Django

Los 4 modelos están registrados en [tesoreria/admin.py](tesoreria/admin.py) con configuración extendida:

```python
@admin.register(CuentaBancaria)   # list_display, list_filter, search_fields
@admin.register(CategoriaMovimiento)
@admin.register(Ingreso)          # date_hierarchy, list_filter, search_fields
@admin.register(Egreso)
```

Acceso: `http://127.0.0.1:8000/admin/`

---

### ✅ Al menos 3 ModelViewSet o GenericAPIView (Django Rest Framework)

Implementados en [tesoreria/views.py](tesoreria/views.py) usando `ModelViewSet` (incluye GET, POST, PUT, PATCH, DELETE):

| # | ViewSet | Endpoint |
|---|---------|----------|
| 1 | `CuentaBancariaViewSet` | `/api/tesoreria/cuentas/` |
| 2 | `CategoriaMovimientoViewSet` | `/api/tesoreria/categorias/` |
| 3 | `IngresoViewSet` | `/api/tesoreria/ingresos/` |
| 4 | `EgresoViewSet` | `/api/tesoreria/egresos/` |

Los ViewSets de `Ingreso` y `Egreso` soportan filtrado por cuenta con `?cuenta=<id>`.

---

### ✅ Al menos 1 Custom API (Django Rest Framework)

Implementada en [tesoreria/views.py](tesoreria/views.py) usando `APIView`:

**`ResumenTesoreriaAPIView`** — `GET /api/tesoreria/resumen/`

Calcula y devuelve por cada cuenta bancaria activa:
- `total_ingresos`: suma de todos los ingresos
- `total_egresos`: suma de todos los egresos
- `saldo_actual`: `saldo_inicial + total_ingresos - total_egresos`

Y como totales globales:
- `total_ingresos_global`
- `total_egresos_global`
- `saldo_neto_global`

Ejemplo de respuesta:
```json
{
  "cuentas": [
    {
      "cuenta_id": 1,
      "nombre": "Caja Principal",
      "banco": "Banco Unión",
      "moneda": "BOB",
      "saldo_inicial": "5000.00",
      "total_ingresos": 3000,
      "total_egresos": 1200,
      "saldo_actual": 6800
    }
  ],
  "totales": {
    "total_ingresos_global": 3000,
    "total_egresos_global": 1200,
    "saldo_neto_global": 6800
  }
}
```

---

### ✅ Archivo requirements.txt en la raíz del repositorio

Ubicado en la raíz del proyecto:

```
asgiref==3.11.1
Django==6.0.3
djangorestframework==3.16.1
psycopg2-binary==2.9.11
sqlparse==0.5.5
```

---

## 3. Estructura del Proyecto

```
usip_modulo5_v8_2026_FCH/
├── ecoapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tesoreria/
│   ├── migrations/
│   ├── admin.py        ← 4 modelos registrados
│   ├── models.py       ← 4 modelos + 2 validaciones
│   ├── serializers.py  ← 4 serializers
│   ├── views.py        ← 4 ModelViewSets + 1 Custom APIView
│   └── urls.py         ← Router DRF + ruta resumen
├── manage.py
├── requirements.txt
├── README.md
└── INFORME_PROYECTO.md
```

---

## 4. Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | 3.9+ | Lenguaje base |
| Django | 6.0.3 | Framework web |
| Django Rest Framework | 3.16.1 | API REST |
| SQLite | — | Base de datos (desarrollo) |

---

## 5. Instrucciones para ejecutar

```sh
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Luego abrir: `http://127.0.0.1:8000/api/tesoreria/`
