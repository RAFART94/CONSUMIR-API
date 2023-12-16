import requests


moneda_cripto = input('Ingrese una criptomoneda conocida:').upper()
apikey = '12586E01-B54C-4500-8495-275C251C63BE'

#Invocando al metodo get con el url especifica
url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}'
r = requests.get(url)

#ejercicio 1, como capturamos el rate
respuesta = r.json()#obtener la respuesta en formato diccionario
#print('rate:',respuesta['rate'])

#ejercicio 2, como capturamos errores de peticion http

if r.status_code == 200:
    print('rate:', respuesta['rate'])
else:
    print('error:', respuesta['error'])

'''
print('Código http de repuesta:', r.status_code)
print('Cabecera:' , r.headers['content-type'])
print('Encoding:', r.encoding)
print('Respuesta en estring', r.text)
print('Respuesta enjson:', r.json())
'''