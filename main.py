# Import das funções de functions.py
from functions import *

# Criação da variável que encerra o While
encerra_while = False

# While para escolher alguma opção válida do menu
while not encerra_while:
    opcao = entradaOpcao()
    encerra_while = validacao(opcao)
