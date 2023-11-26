# Import das funções de functions.py
from functions import chamarMenu, validacao

# While para o programa não terminar até o usuário escolher sair dele
while True:
    # Criação da variável que encerra o While de validação abaixo
    encerra_while = False

    # While para escolher alguma opção válida do menu
    while not encerra_while:
        # Chama a função do menu e armazena o resultado na variável 'opcao'
        opcao = chamarMenu()
        # Chama a função 'validacao' e utiliza seu resultado para encerrar ou não o while
        encerra_while = validacao(opcao)
