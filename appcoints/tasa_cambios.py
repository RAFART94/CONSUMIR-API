import requests
from utils import config

moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()

while moneda_cripto != '' and moneda_cripto.isalpha():
#Invocando al metodo get con el url especifica
    url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}'
    r = requests.get(url)

    #ejercicio 1, como capturamos el rate
    respuesta = r.json()#obtener la respuesta en formato diccionario
    #print('rate:',respuesta['rate'])

#ejercicio 2, como capturamos errores de peticion http

    if r.status_code == 200:
        #print('rate:', respuesta['rate']) #2046.4276214444258 cambie a 2046.43€
        print('{:.2f}€'.format(respuesta['rate'])) #2046.43€
        break
    else:
        print('error:', respuesta['error'])

    moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()