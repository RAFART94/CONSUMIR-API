
class Views():
    def insertCoin(self):
        moneda_cripto = input('Ingrese una moneda conocida: ').upper()
        return moneda_cripto
    
    def viewListCoins(self, allcoins):
        print(f'Total: {len(allcoins.lista_general)} \nCriptos: {len(allcoins.lista_criptos)} \nNo Criptos: {len(allcoins.lista_no_criptos)}')

    def viewRateExchange(self, change):
        print(f'fecha de consulta:{change.time} '+'\n{:.2f}€'.format(change.rate))
    
    def viewRateExchange2(self, change):
        print(f'fecha de consulta:{change.time} \n{change.rate}')

    def getError(self, er):
        print(er)
