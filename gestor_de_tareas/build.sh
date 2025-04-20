#!/usr/bin/env bash

# Salir si ocurre un error
set -o errexit

# Ejecutar migraciones de la base de datos
python manage.py migrate

# Colectar archivos estáticos (por si usás css/js en templates)
python manage.py collectstatic --noinput
