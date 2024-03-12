# pda_registry_service
Servicio de PDA que se utiliza para el registro de propiedades a analizar.

## consideraciones previas

El servicio de pulsar debe estas funcionando, se sugiere utilizar la estructura de este docker-compose.yml
```python
version: '3.1'
services:
  pulsar:
    image: apachepulsar/pulsar:latest
    container_name: pulsar-standalone
    ports:
      - "6650:6650"
      - "8080:8080"
    volumes:
      - ./data:/pulsar/data
    command: bin/pulsar standalone
```

Y luego ejecutarlo de la siguiente manera
```python
docker-compose -f "docker-compose.yml" up
```

Este repositorio fue escrito en python v3.10.12, para instalar las librerias se debe lanzar
```python
pip install -r requirements.txt
```

## debe tener un archivo .env
tomar el archivo .env.example y renombrarlo .env, luego se deben colocar las variables necesarias

## levantar la base de datos
el docker ya lee de variables de entorno si y solo si el archivo se llama .env, por lo tanto el paso anterior ya debe estár completado
```python
docker-compose -f "docker-compose.yml" up
```

## ejecutar el servidor
se deben cargar las variables de entorno en el ambiente
```python
export $(cat .env)
```
Luego se procede a levantar el servidor
```python
gunicorn src.auditoria.api:app --bind 0.0.0.0:3010
```

## endpoint para crear una propiedad

endpoint: http://localhost:3001/async-propiedad

tipo: POST
body
```json
{
    "nombre": "casa estrella",
    "coordenadas": {"lat": 123, "lng": 456},
    "direccion": "calle 100 N 12-12",
    "fecha_creacion": "2024-01-01"
}
```

## endpoint estado de salud del servicio.
http://localhost:3001/catastro/health

## Contribución

Alexander contreras