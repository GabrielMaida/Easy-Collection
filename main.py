from functions import *
import sys
import time

encerra_while = False

while encerra_while == False:
    opcao = entradaOpcao()

    match opcao:
        case '1':
            try:
                adicionarDados()
                print('Dado adicionado com sucesso!')
                encerra_while = True
            except:
                print('Ocorreu um erro ao adicionar o dado!')
        case '2':
            try:
                lerDados()
                print('Dados lidos com sucesso!')
                encerra_while = True
            except:
                print('Ocorreu um erro ao ler os dados!')
        case '3':
            try:
                atualizarDados()
                print('Dados atualizados com sucesso!')
                encerra_while = True
            except:
                print('Ocorreu um erro ao atualizar os dados!')
        case '4':
            try:
                excluirDados()
                print('Dados excluídos com sucesso!')
                encerra_while = True
            except:
                print('Ocorreu um erro ao excluir os dados!')
        case '5':
            print('Saindo do programa...')
            sys.exit()
        case _:
            print('Opção inválida!')
            print('.')
            time.sleep(0.4)
            print('.')
            time.sleep(0.4)
            print('.')
            time.sleep(0.4)