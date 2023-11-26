# Imports do arquivo
from sys import exit
from time import sleep


###############################################################


# Função para mostrar o menu de opções
def chamarMenu():
    print(10 * "-", "Opções", 10 * "-")
    print("1- Adicionar dados")
    print("2- Ler dados")
    print("3- Atualizar dados")
    print("4- Excluir dados")
    print("5- Realizar backup dos dados")
    print("0- Sair do programa")
    print(28 * "-")

    # Salvar a escolha do usuário em uma variável
    escolha = str(input("Digite a opção desejada: "))

    # Retornar a escolha do usuário
    return escolha


###############################################################


# Função para validar a opção escolhida pelo usuário
def validacao(escolha):
    match escolha:
        case "1":
            try:
                # Chama a função para adicionar dados
                adicionarDados()
                print("\nLivros adicionados com sucesso!")
                return True
            except Exception:
                print("Ocorreu um erro ao cadastrar o livro!")
        case "2":
            try:
                # Chama a função para ler dados
                lerDados()
                print("\nDados lidos com sucesso!")
                input("\nPressione Enter para continuar...")
                return True
            except Exception:
                print("Ocorreu um erro ao ler os dados!")
        case "3":
            try:
                # Chama a função para atualizar dados
                atualizarDados()
                print("\nDado atualizado com sucesso!")
                return True
            except Exception:
                print("Ocorreu um erro ao atualizar os dados!")
        case "4":
            try:
                # Chama a função para excluir dados
                excluirDados()
                print("\nLivro excluído com sucesso!")
                return True
            except Exception:
                print("Ocorreu um erro ao excluir o livro!")
        case "5":
            try:
                # Chama a função para fazer backup dos dados
                backupDados()
                print("\nBackup realizado com sucesso!")
                return True
            except Exception:
                print("Ocorreu um erro ao realizar o backup dos dados!")
        case "0":
            # Sai do programa
            print("Saindo do programa...")
            exit()
        case _:
            print("Opção inválida!")
            print(".")
            sleep(0.4)
            print(".")
            sleep(0.4)
            print(".")
            sleep(0.4)
            return False


###############################################################


# Função para gravar novos dados
def adicionarDados():
    # Definição da variável responsável pela quebra dos whiles
    variavel_continuar_adicao = "s"

    # While para adição de novos dados até o usuário digitar "n"
    while variavel_continuar_adicao == "s":
        # Entrada dos dados por parte do usuário
        livro = str(input("Livro: "))
        autor = str(input("Autor: "))

        # Formatação dos dados digitados em uma string
        dados_salvos = f"{livro} - {autor}\n"

        # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
        # Cria o arquivo caso não exista
        with open("livros.txt", "a", encoding="utf-8") as arquivo_txt:
            arquivo_txt.write(dados_salvos)

        # Pergunta se deseja continuar a gravação e registra 's' ou 'n'
        variavel_continuar_adicao = str(input("Deseja adicionar mais livros? [s/n] ")).lower()

        # Tratamento de exceção do [s/n]
        while variavel_continuar_adicao not in ["s", "n"]:
            print("Opção inválida! Tente novamente...")
            sleep(1)
            variavel_continuar_adicao = str(input("Deseja adicionar mais livros? [s/n] ")).lower()


###############################################################


# Função para ler os dados gravados
def lerDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Salva a quantidade de linhas do arquivo dentro da variável 'quantidade_linhas'
    quantidade_linhas = (len(linhas))

    # No caso de não houverem dados dentro do arquivo
    if not linhas:
        print("Nenhum livro registrado!")
        sleep(0.5)
    elif quantidade_linhas == 1:
        print(f"O banco de dados possui {quantidade_linhas} livro:\n")
        sleep(0.5)
    else:
        print(f"O banco de dados possui {quantidade_linhas} livros:\n")
        sleep(0.5)

    # Abre a variável 'indice' para a impressão do índice do dado na tela
    indice = 1

    # Para cada linha no arquivo, imprime seus dados na tela
    for linha in linhas:
        print(f"{indice}- " + linha, end="")
        sleep(0.1)
        indice += 1


###############################################################


# Função para atualizar dados
def atualizarDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Salva a quantidade de linhas do arquivo dentro da variável 'quantidade_linhas'
    quantidade_linhas = (len(linhas))
    # If para diferenciação entre 1 ou mais dados
    if quantidade_linhas == 1:
        print(f"O banco de dados possui {quantidade_linhas} livro")
    else:
        print(f"O banco de dados possui {quantidade_linhas} livros")
    lerDados()

    # Variável para registrar qual dado o usuário irá editar
    indice = int(input("Escolha qual livro você quer editar: "))

    # Variável para salvar o novo valor
    novo_valor = str(input("Escolha o novo valor: "))

    # Abre o arquivo 'livros.txt' no modo escrita e fecha após o uso
    with open("livros.txt", "w") as arquivo_txt:
        # Salva o novo valor na linha (indice - 1)
        linhas[indice - 1] = f"{novo_valor}\n"
        # Escreve o novo valor na linha propriamente
        arquivo_txt.writelines(linhas)

    # Printa o novo valor na tela
    print(f"{indice}- " + linhas[indice - 1])


###############################################################


# Função para excluir dados
def excluirDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Salva a quantidade de linhas do arquivo dentro da variável 'quantidade_linhas'
    quantidade_linhas = (len(linhas))
    # If para diferenciação entre 1 ou mais dados
    if quantidade_linhas == 1:
        print(f"O banco de dados possui {quantidade_linhas} livro")
    else:
        print(f"O banco de dados possui {quantidade_linhas} livros")

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
    print(f"Livro número {indice} excluído")


#########################################


def backupDados():
    # Abre o arquivo 'livros.txt' no modo leitura e fecha após o uso
    with open("livros.txt", "r") as arquivo_txt:
        # Grava no formato de texto os dados de 'livros.txt' na variável 'linhas'
        linhas = arquivo_txt.readlines()

    # Abre o arquivo 'backup.txt' no modo escrita e fecha após o uso
    # O arquivo será criado caso não exista
    with open("backup.txt", "w") as backup:
        # Grava os dados salvos em 'linhas' no arquivo 'backup.txt'
        backup.writelines(linhas)
