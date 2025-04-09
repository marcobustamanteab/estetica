FROM python:3.9-slim

WORKDIR /app

# Copia todo el contenido actual del repositorio al contenedor
COPY . .

# Instala las dependencias
RUN cd backend && pip install -r requirements.txt

# Configura variables de entorno
ENV PYTHONUNBUFFERED=1

# Ejecuta migraciones y servidor
WORKDIR /app/backend
RUN python manage.py collectstatic --noinput
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000}