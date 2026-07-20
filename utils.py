import os

def limpar_tela():

    os.system('cls')


def pausar():
    input("\nPressione ENTER para continuar...")


def proibir_vazio(mensagem):

    while True:

        texto = input(mensagem).strip()

        if texto:
            return texto 
        
        print("O campo não pode ficar vazio.")


def ler_opcao(mensagem):

    while True:

        try:
            return int(input(mensagem))

        except ValueError:
            print('Escolha uma opção válida')
           

def ler_enum(enum, mensagem):

    while True:

        try:
            valor = int(input(mensagem))
            return enum(valor)

        except ValueError:
            print("Escolha uma opção válida.")

