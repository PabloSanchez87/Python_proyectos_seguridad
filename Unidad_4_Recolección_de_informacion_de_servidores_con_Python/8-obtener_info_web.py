#!/usr/bin/python

import requests
import os

API_KEY = os.getenv("WHO_API_KEY")

def whois(dominio=None):
	try:
		parametros = {'domain': dominio}
		cabeceras = {
                "Host": "api.whoapi.com"
                }
		respuesta = requests.get('http://api.whoapi.com/?domain=%s'% parametros['domain'] + '&r=whois&apikey=' + API_KEY,params=parametros, headers=cabeceras)
		print(respuesta.status_code)
		datos = respuesta.text
		return(respuesta.json())
	except Exception as exception:
		print("Error: ",exception)
		
resultado = whois('python.org')

for key, value in resultado.items():
	print(str(key) + '<--->' + str(value))		

