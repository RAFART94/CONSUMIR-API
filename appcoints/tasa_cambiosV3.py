from config import APIKEY
from model import *

#consulta de todas las monedas
allcoins = AllCoinsApiIO()
allcoins.getAllCoins(APIKEY)

print('Total: ',len(allcoins.lista_general))
print('Criptos: ', len(allcoins.lista_criptos))
print('No Criptos: ', len(allcoins.lista_no_criptos))
##############################################################
moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()

while moneda_cripto != '' and moneda_cripto.isalpha():
    if moneda_cripto in allcoins.lista_criptos:
        exchange = Exchange(moneda_cripto)
        try:
            exchange.updateExchange(APIKEY)
            print('{:.2f}€'.format(exchange.rate))
        except ModelError as error:
            print(error)

    moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()
