from appcoints.config import APIKEY
from appcoints.model import *
from appcoints.view import *

class AppCoinsController():
    def executeProgram(self):
        #consulta de todas las monedas
        allcoins = AllCoinsApiIO()#Creando objeto
        viewTools = Views()#Creando objetos
        allcoins.getAllCoins(APIKEY)


        viewTools.viewListCoins(allcoins=allcoins)
        ##############################################################
        moneda_cripto = viewTools.insertCoin()

        while moneda_cripto != '' and moneda_cripto.isalpha():
            if moneda_cripto in allcoins.lista_no_criptos:
                exchange = Exchange(moneda_cripto)
                try:
                    exchange.updateExchange2(APIKEY)
                    viewTools.viewRateExchange2(exchange)
                except ModelError as error:
                    viewTools.getError(error)

            moneda_cripto = viewTools.insertCoin()
