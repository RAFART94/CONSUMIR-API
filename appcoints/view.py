
class Views():
    def insertCoin(self):
        moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()
        return moneda_cripto
    
    def viewListCoins(self, allcoins):
        print('Total: ',len(allcoins.lista_general))
        print('Criptos: ', len(allcoins.lista_criptos))
        print('No Criptos: ', len(allcoins.lista_no_criptos))

    def viewRateExchange(self, change):
        print('{:.2f}€'.format(change.rate))

    def getError(self, er):
        print(er)