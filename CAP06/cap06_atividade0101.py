"""
    Introdução à funções no Python.
    Comando: def

    toda função deve ser definada (criada) no início da aplicação (escopo global)
"""

from os import system, name
system('cls') if (name == 'nt') else system('clear')

def soma(v1, v2, item):
    if item == 1:

    return int(v1)+int(v2)

n1 = input(f'Informe o 1º número.: ')
n2 = input(f'Informe o 2º número.: ')
print('')
opcoes = ("Soma", "Subtração", "Multiplicação", "Divisão")
print('Suas opções para o cálculo são.: ')
for i, elemento in enumerate(opcoes):
    print(f'{i+1} - {elemento}')
    print('')

escolha = int(input('Agora escolha sua opção de cálculo!.: '))-1



print(f'A soma de {n1} e {n2} é igual a {soma(n1, n2, escolha)}')

