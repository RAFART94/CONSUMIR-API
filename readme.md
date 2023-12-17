## Aplicación de consulta de valor actual de criptomonedas

Programa hecho en python para recuperar el valor en euros de una criptomoneda
desde www.coinapi.io

# Instalación
-Obtener una API key en www.coinapi.io
-Renombrar el fichero config_template.py a config.py
-Agregar dentro de aconfig.py el API key de esta manera:

```
APIKEY = 'AQUI VA SU APIKEY'
```

## Instalación de dependencias(librerias)
-Crear un entorno virtual de python
```
python -m venv entorno
py -m venv entorno
python3 -m venv entorno
```

-Activar el entorno e intalar los requerimientos
```
windows - .\entorno\Scritps\activate
mac o linux - source entorno/bin/activate

pip install -r requirements.txt
```