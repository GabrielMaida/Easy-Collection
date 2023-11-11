# Imports do arquivo
import time
import sys


###############################################################


# Definição das variáveis das cores
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
restaurar_cor = '\033[0;0m'


###############################################################


# Função para mostrar o menu de opções
def entradaOpcao():
    print(10 * '-', 'Opções', 10 * '-')
    print('1- Adicionar dados')
    print('2- Ler dados')
    print('3- Atualizar dados')
    print('4- Excluir dados')
    print('5- Sair do programa')
    print(28 * '-')

    # Salvar a escolha do usuário em uma variável
    escolha = str(input('Digite a opção desejada: '))

    # Retornar a escolha do usuário
    return escolha


###############################################################


# Função para validar a opção escolhida pelo usuário
def validacao(escolha):
    match escolha:
        case '1':
            try:
                adicionarDados()
                print('Dado adicionado com sucesso!')
                return True
            except ValueError:
                print('Ocorreu um erro ao adicionar o dado!')
        case '2':
            try:
                lerDados()
                print('Dados lidos com sucesso!')
                return True
            except ValueError:
                print('Ocorreu um erro ao ler os dados!')
        case '3':
            try:
                atualizarDados()
                print('Dados atualizados com sucesso!')
                return True
            except ValueError:
                print('Ocorreu um erro ao atualizar os dados!')
        case '4':
            try:
                excluirDados()
                print('Dados excluídos com sucesso!')
                return True
            except ValueError:
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
            return False


###############################################################


# Função para gravar novos dados
def adicionarDados():
    # Definição das variáveis responsáveis pela quebra dos whiles
    variavel_continuar_adicao = 's'

    # While para adição de novos dados até o usuário digitar 'n'
    while variavel_continuar_adicao == 's':
        # Atribuição dos dados
        nome = str(input('Nome: '))
        sexo = str(input('Sexo: '))

        # Formatação dos dados em uma string
        dados_salvos = f"{nome} - {sexo}\n"

        # Gravação dos dados no arquivo de texto
        with open('usuarios.txt', 'a', encoding='utf-8') as arquivo_txt:
            arquivo_txt.write(dados_salvos)

        # Perguntar se deseja continuar a gravação
        variavel_continuar_adicao = str(input('Deseja adicionar mais dados? [s/n] ')).lower()

        # Tratamento de exceção do [s/n]
        while variavel_continuar_adicao not in ['s', 'n']:
            print('Opção inválida! Tente novamente...')
            time.sleep(1)
            variavel_continuar_adicao = str(input('Deseja adicionar mais dados? [s/n] ')).lower()


###############################################################


# Função para ler os dados gravados
def lerDados():
    with open('usuarios.txt', 'r') as arquivo_txt:
        linhas = arquivo_txt.readlines()

        if not linhas:
            print('Nenhum dado registrado!')
            time.sleep(1)
        else:
            print('Dados registrados:\n')
            time.sleep(0.2)

        i = 1
        for linha in linhas:

            print(f'{i}- ' + linha)
            time.sleep(0.1)
            i += 1


###############################################################


# Função para atualizar dados
def atualizarDados():
    with open('usuarios.txt', 'r') as arquivo_txt:
        linhas = arquivo_txt.readlines()

    quantidade_linhas = (len(linhas))

    print(f'O banco possui {quantidade_linhas} valores')
    lerDados()

    indice = int(input('Escolha qual valor você quer editar: '))

    novo_valor = str(input('Escolha o novo valor: '))

    with open('usuarios.txt', 'w') as arquivo_txt:
        linhas[indice-1] = f'{novo_valor}\n'
        arquivo_txt.writelines(linhas)

    print(f'{indice}- ' + linhas[indice-1])


###############################################################


# Função para excluir dados
def excluirDados():
    with open('usuarios.txt', 'r') as arquivo_txt:
        linhas = arquivo_txt.readlines()

    quantidade_linhas = (len(linhas))

    print(f'O banco possui {quantidade_linhas} valores')
    lerDados()

    indice = int(input('Escolha qual valor você quer excluir: '))

    with open('usuarios.txt', 'w') as arquivo_txt:
        del linhas[indice-1]
        arquivo_txt.writelines(linhas)

    print(f'Dado número {indice} excluído')
