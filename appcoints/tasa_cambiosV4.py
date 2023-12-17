from config import APIKEY
from model import *
from view import *

#consulta de todas las monedas
allcoins = AllCoinsApiIO()#Creando objeto
viewTools = Views()#Creando objetos
allcoins.getAllCoins(APIKEY)


viewTools.viewListCoins(allcoins=allcoins)
##############################################################
moneda_cripto = viewTools.insertCoin()

while moneda_cripto != '' and moneda_cripto.isalpha():
    if moneda_cripto in allcoins.lista_criptos:
        exchange = Exchange(moneda_cripto)
        try:
            exchange.updateExchange(APIKEY)
            viewTools.viewRateExchange(exchange)
        except ModelError as error:
            viewTools.getError(error)

    moneda_cripto = viewTools.insertCoin()
