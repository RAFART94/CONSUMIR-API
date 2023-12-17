from appcoints.model import AllCoinsApiIO, Exchange, ModelError
from appcoints.config import APIKEY
import pytest

def test_allcoins():
    listas = AllCoinsApiIO()#Creando objeto de la clase AllCoinsApiIO
    listas.getAllCoins(APIKEY)#Llamando al metodo getAllCoins()
    assert listas != None #True
    cantidad = len(listas.lista_criptos) + len(listas.lista_no_criptos)
    assert cantidad == 18531 #True

def test_exchange():
    cambio = Exchange('EUR')
    cambio.updateExchange(APIKEY)
    assert cambio.rate > 0 #True
    assert cambio.rate != None #True

def test_exchange_error():
    cambio = Exchange('ÑÑÑ')
    
    with pytest.raises(ModelError) as exceptioInfo:
        cambio.updateExchange(APIKEY)
    assert str(exceptioInfo.value) == f"status:{cambio.status_code}, error: You requested specific single item that we don\u0027t have at this moment."
    assert cambio.status_code