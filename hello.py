#!/usr/bin/env python3
''' 

Hello World Multi Linguas.


Dependendo do lingua configurada no ambiente

o programa exibe a mensagem correspondente. 


Como usar: 


Tenha a variável LANG  devidamente configurada ex: 


    LANG = pt-BR

'''


__version__ = "0.0.1"

__author__ = "Daiane Ucceli"

__license__ = "UNlicense"

#Progama imprime hello world

import os

current_language = os.getenv("LANG", "en_US") [:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)


