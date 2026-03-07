
from os import system, name

def limparTela():
    system('cls') if (name == 'nt') else system('clear')

def menucabecalho():
    print("* * * * * *".center(200,"="))
    print(' * * -- A T I V I D A D E -- * * '.center(200," ")) #substituir pelo nome da atividade
    print('='.center(200,"="))
    print()

def menuopcoes():
    print(f'''
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
            ''') 

limparTela()
menucabecalho()
