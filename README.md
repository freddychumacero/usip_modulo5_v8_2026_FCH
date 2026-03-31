# Sistema de Gestión de Tesorería

**Autor:** Freddy Einard Chumacero Cors  
**Curso:** Módulo V — Django  
**Institución:** USIP

---

## Descripción

Aplicación web desarrollada con **Django** y **Django Rest Framework** para la gestión de tesorería de una pequeña empresa. Permite registrar cuentas bancarias, categorizar movimientos, registrar ingresos y egresos, y consultar el saldo neto por cuenta.

---

## Requisitos previos

- Python 3.9+
- pip

Se recomienda usar un entorno virtual:

```sh
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## Instalar dependencias

```sh
pip install -r requirements.txt
```

## Aplicar migraciones

```sh
python3 manage.py migrate
```

## Crear superusuario (acceso al Admin)

```sh
python3 manage.py createsuperuser
```

## Ejecutar servidor de desarrollo

```sh
python3 manage.py runserver
```

---

## Accesos

| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/admin/` | Panel de administración Django |
| `http://127.0.0.1:8000/api/tesoreria/` | Raíz de la API REST |
| `http://127.0.0.1:8000/api/tesoreria/cuentas/` | CRUD Cuentas Bancarias |
| `http://127.0.0.1:8000/api/tesoreria/categorias/` | CRUD Categorías de Movimientos |
| `http://127.0.0.1:8000/api/tesoreria/ingresos/` | CRUD Ingresos |
| `http://127.0.0.1:8000/api/tesoreria/egresos/` | CRUD Egresos |
| `http://127.0.0.1:8000/api/tesoreria/resumen/` | Resumen de tesorería (Custom API) |

---

## Modelos

- **CuentaBancaria** — banco, número de cuenta, moneda (BOB/USD/EUR), saldo inicial
- **CategoriaMovimiento** — nombre y tipo (ingreso / egreso)
- **Ingreso** — monto, fecha, cuenta, categoría, descripción
- **Egreso** — monto, fecha, cuenta, categoría, descripción

## Validaciones personalizadas

- `monto` debe ser mayor a 0
- `fecha` no puede ser futura

---

## Stack tecnológico

- Django 6.0.3
- Django Rest Framework 3.16.1
- SQLite (desarrollo)
