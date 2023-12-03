# Imports do arquivo
from sys import exit  # Importa a função exit() para sair do programa
from time import sleep  # Importa a função sleep() para dar um delay no programa
from datetime import datetime  # Importa a função datetime() para obter a data e hora atual


###############################################################


# Função para mostrar o menu de opções
def chamarMenu():
    try:
        # While para o programa não terminar exceto se o usuário escolher
        while True:
            print(10 * "-", "Opções", 10 * "-")
            print("1- Adicionar dados")
            print("2- Ler dados")
            print("3- Atualizar dados")
            print("4- Excluir dados")
            print("5- Realizar backup dos dados")
            print("0- Sair do programa")
            print(28 * "-")

            # Salvar a escolha do usuário em uma variável
            opcao = str(input("Digite a opção desejada: "))
            # Chama a função de validação para verificar se a opção é válida
            validacao(opcao)
    except KeyboardInterrupt:
        print("\nSaindo do programa...")
        exit()


###############################################################


# Função para validar a opção escolhida pelo usuário
def validacao(escolha):
    match escolha:
        case "1":
            adicionarDados()
        case "2":
            lerDados()
        case "3":
            atualizarDados()
        case "4":
            excluirDados()
        case "5":
            backupDados()
        case "0":
            print("Saindo do programa...")
            exit()
        case _:
            print("Opção inválida!")
            print(".\n.\n.")
            sleep(0.5)


###############################################################


# Função para gravar novos dados
def adicionarDados():
    # Definição da variável responsável pela quebra do while
    variavel_continuar_adicao = "s"

    # While para adição de novos dados até o usuário digitar "n"
    while variavel_continuar_adicao == "s":

        # Inserção do nome do livro com tratamento de exceção
        livro = str(input("Livro: "))
        while not livro.replace(" ", "").isalnum():
            print("Caracteres inválidos. Digite apenas alfanuméricos.")
            livro = str(input("Livro: "))

        # Inserção do nome do autor com tratamento de exceção
        autor = str(input("Autor: "))
        while not autor.replace(" ", "").isalpha():
            print("Caracteres inválidos. Digite apenas letras.")
            autor = str(input("Autor: "))

        # Obtendo a data e hora atual
        data_formatada = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Formatação dos dados digitados em uma string
        dados_salvos = f"{livro} - {autor} - {data_formatada}\n"

        # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
        # Cria o arquivo caso não exista
        with open("livros.txt", "a", encoding="latin-1") as arquivo_txt:
            arquivo_txt.write(dados_salvos)

        print("\nLivro adicionado com sucesso!\n")

        # Pergunta se deseja continuar a gravação e registra 's' ou 'n'
        variavel_continuar_adicao = str(input("Deseja adicionar mais livros? [s/n] ")).lower()
        # Tratamento de exceção do [s/n]
        while variavel_continuar_adicao not in ["s", "n"]:
            print("Opção inválida! Tente novamente...")
            sleep(0.5)
            variavel_continuar_adicao = str(input("Deseja adicionar mais livros? [s/n] ")).lower()


###############################################################


# Função para ler os dados gravados
def lerDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Tratamento de exceção para caso o arquivo não tenha nada
    if not linhas:
        print("Não há nada salvo para realizar backup")
        return

    # Salva a quantidade de linhas do arquivo dentro da variável 'quantidade_linhas'
    quantidade_linhas = (len(linhas))
    # If para diferenciação entre 1, vários ou nenhum dados salvos
    if quantidade_linhas == 1:
        print(f"O banco de dados possui {quantidade_linhas} livro:\n"+'-'*70)
    elif quantidade_linhas > 1:
        print(f"O banco de dados possui {quantidade_linhas} livros:\n"+'-'*70)
    else:
        print(f"O banco de dados não possui livros cadastrados")
        return
    print(f"|"+" "*31+"Livros"+" "*30+"|\n"+"-"*70)

    # Abre a variável 'indice' para a impressão do índice do dado na tela
    indice = 1

    for linha in linhas:
        dados = linha.strip().split(' - ')
        print(f'| {indice} | Nome: {dados[0]} | Autor: {dados[1]} | Data: {dados[2]} |')
        print('-'*70)
        indice += 1
        sleep(0.1)

    print("\nDados lidos com sucesso!\n")


###############################################################


# Função para atualizar dados
def atualizarDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Tratamento de exceção para caso o arquivo não tenha nada
    if not linhas:
        print("Não há nada salvo para atualizar")
        return

    # Chama a função de ler dados para mostrá-los na tela
    lerDados()

    # Variável para registrar qual dado o usuário irá editar
    indice = int(input("Escolha qual livro você quer editar: ")) - 1
    # Variável para comparar com o índice escolhido pelo usuário
    contador = 0

    # Laço de repetição para percorrer todas as linhas do arquivo
    for _ in linhas:
        # Obtendo a data e hora atual
        data_formatada = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Comparação para analisar se o for está na linha que o usuário quer editar
        if contador == indice:
            # Solicita ao usuário os novos valores
            novo_nome = input("Escolha o novo nome do livro: ")
            novo_autor = input("Escolha o novo nome do autor: ")
            # Cria a nova linha com os dados atualizados
            nova_linha = f"{novo_nome} - {novo_autor} - {data_formatada}\n"
            # Substitui a linha antiga pela nova
            linhas[indice] = nova_linha
        contador += 1

    # Abre o arquivo 'livros.txt' no modo escrita e fecha após o uso
    with open("livros.txt", "w") as arquivo_txt:
        arquivo_txt.writelines(linhas)

    print("\nDado atualizado com sucesso!\n")


###############################################################


# Função para excluir dados
def excluirDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Tratamento de exceção para caso o arquivo não tenha nada
    if not linhas:
        print("Não há nada salvo para excluir")
        return

    # Chama a função de ler dados para mostrá-los na tela
    lerDados()

    # Variável para registrar qual dado o usuário irá excluir
    indice = int(input("Escolha qual livro você quer excluir: "))

    # Abre o arquivo 'livros.txt' no modo escrita e fecha após o uso
    with open("livros.txt", "w") as arquivo_txt:
        # Deleta a linha de valor (indice - 1)
        del linhas[indice - 1]
        # Escreve a edição no arquivo propriamente
        arquivo_txt.writelines(linhas)

    # Printa o índice do dado excluído
    print(f"Livro {indice} excluído com sucesso\n")


#########################################


def backupDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Tratamento de exceção para caso o arquivo não tenha nada ou não exista
    if not linhas:
        print("Não há nada salvo para realizar backup")
        return

    # Abre o arquivo 'backup.txt' no modo escrita e fecha após o uso
    # O arquivo será criado caso não exista ou substituirá o antigo
    with open("backup.txt", "w") as backup:
        # Grava os dados salvos em 'linhas' no arquivo 'backup.txt'
        backup.writelines(linhas)

    print("\nBackup realizado com sucesso!\n")
