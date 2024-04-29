# py-data-server
Servidor en python que genera datos simulando trafico de red

## Necesario
- Python3.10 o superior
- PIP3
- Pytenv

## Uso

- Para usar necesitamos instalar las librerias por ello iniciamos un repositorio con `git init` donde instalaremos un entorno virtual `python3 -m venv venv` para iniciarlo usamos `source ./venv/bin/activate`
- Ahora instalamos las librerias con `pip3 install -r requirements.txt`
- El servidor esta usando FastApi para crear la API y Uvicorn para levantar el servicio en el puerto 8000
- Iniciamos el servidor `uvicorn main:app --reload` con esto podemos ver que se generan solicitudes en `http://localhost:8000 veremos la api funcionando`

## NOTA

- La API es una idea provisoria, aun falta para el funcionamiento correcto. **NO ES PARA USAR EN PRODUCCION TANTO POR SEGURIDAD COMO POR FUNCIONAMIENTO** 
