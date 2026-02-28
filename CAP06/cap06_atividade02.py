
from os import system, name
from calculadora import soma, sub, mult, div
#from calculadora import *

def limparTela():
    system('cls') if (name == 'nt') else system('clear')

def menu():
    print("\n Escolha a operação aritimática desejada!!!")
    print(f'''
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
            ''')    

def menu1():
    print('- OPERAÇÕES ARITIMÉTICAS -'.center(200,"*"))
    print('='.center(200,"="))
    print()
    #input()

while (True):
    limparTela()
    menu1()
    #menu()
    try:
        n1 = float(input('Informe o 1º valor.: '))
        n2 = float(input('Informe o 2º valor.: ')) 
        menu()
    except ValueError:
        print('Opção inválida. Informe somente números')
        input()
        #menu()
        continue

    
    while (True):
        operador = input('Opção.: ')
        if operador in ["1","2","3","4"]:
            operador = int(operador)
            break
        else:
            print("Opção inválida.! Escolha entre 1 e 4.")
            input('\nAcione qualquer tecla para continuar..!!')
            limparTela()
            menu1()
            print(f'Informe o 1º valor.: {int(n1)}')
            print(f'Informe o 1º valor.: {int(n2)}')
            menu()
        
    if operador==1:
        soma(n1,n2)
    elif operador==2:
        sub(n1,n2)
    elif operador==3:
        mult(n1,n2)
    elif operador==4:
        div(n1,n2)
        
    opcao = input('Digite qualquer tecla para continuar ou "X" para encerrar.')
    if opcao.upper()=='X':
        break
    
