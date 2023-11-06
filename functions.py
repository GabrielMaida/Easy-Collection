import time

#Função para mostrar o menu de opções
def entradaOpcao():
    print(10*'-','Opções',10*'-')
    print('1- Adicionar dados')
    print('2- Ler dados')
    print('3- Atualizar dados')
    print('4- Excluir dados')
    print('5- Sair do programa')
    print(28*'-')

    #Salvar a escolha do usuário em uma variável
    escolha = str(input('Digite a opção desejada: '))

    #Retornar a escolha do usuário
    return escolha



#Função para a gravação dos dados
def adicionarDados():
    #Definição das variáveis responsáveis pela quebra dos whiles
    variavel_finalizar_adicao = 's'
    idade = 0

    #While para adição de novos dados até o usuário digitar 'n'
    while variavel_finalizar_adicao == 's' :
        #Atribuição dos dados
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        #Tratamento de exceção da idade
        if idade > 130 or idade < 0:
            while idade > 130 or idade < 0:
                print('Idade inválida! Ela deve estar entre 0 e 130. Digite novamente...')
                time.sleep(1)
                idade = int(input('Idade: '))
        sexo = str(input('Sexo: '))

        #Formatação dos dados em uma string
        dados_salvos = f"{nome} - {idade} - {sexo}\n"

        #Gravação dos dados no arquivo de texto
        with open('usuarios.txt','a',encoding='utf-8') as arquivo_txt:
            arquivo_txt.write(dados_salvos)

        #Resetar a variável para um valor fora do while para ele voltar a funcionar
        idade = -1

        #Perguntar se deseja continuar a gravação
        variavel_finalizar_adicao = str(input('Deseja adicionar mais dados? [s/n] ')).lower()
        #Tratamento de exceção do [s/n]
        if variavel_finalizar_adicao != 'n' and variavel_finalizar_adicao != 's':
            while variavel_finalizar_adicao != 'n' and variavel_finalizar_adicao != 's':
                print('Opção inválida! Tente novamente...')
                time.sleep(1)
                variavel_finalizar_adicao = str(input('Deseja adicionar mais dados? [s/n] ')).lower()



#Função para leitura dos dados
def lerDados():
    pass
with open('usuarios.txt','r') as arquivo_txt:
    pass





def atualizarDados():
    pass

def excluirDados():
    pass
