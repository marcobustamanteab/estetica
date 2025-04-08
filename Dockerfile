FROM python:3.9-slim

WORKDIR /app

# Copia solo los archivos necesarios primero para aprovechar el caché
COPY backend/requirements.txt /app/requirements.txt

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY backend/ /app/

# Configura variables de entorno
ENV PYTHONUNBUFFERED=1

# Ejecuta migraciones y servidor
RUN python manage.py collectstatic --noinput
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT