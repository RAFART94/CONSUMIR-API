respuesta = {
  "time": "2023-12-16T19:08:34.0000000Z",
  "asset_id_base": "BTC",
  "asset_id_quote": "EUR",
  "rate": 39018.293134096815749228248078
}

#print(respuesta['rate'])
#print(respuesta.get('rate'))

errores = {
  "error": "You didn\u0027t specify API key or it is incorrectly formatted. You should do it in: query string parameter \u0060apikey\u0060,  in http header named \u0060X-CoinAPI-Key\u0060,  in http header named \u0060Authorization\u0060 or  as part of URL /apikey-YOUR-API-KEY/"
}

#print(errores['error'])

prueba = 'hdh'
#print(prueba.upper())
#print(prueba.isalpha())#True

numero = 2046.4276214444258
print(type(numero))
valor = '{:,.2f}€'.format(numero)
print(type(valor))
print (valor)