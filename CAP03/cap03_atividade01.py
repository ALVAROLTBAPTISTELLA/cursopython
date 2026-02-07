"""
    Cap03 - Atividade 01
    Verificar número par ou ímpar

    Objetivos:
    Nesta atividade você vai usar uma estrutura de decisão (if / else) para verificar se um númeri é par ou ímpar.

    Comandos utilizados:
    If, operador % (retorna o resto da divisão entre operadores)

"""

import os
os.system('cls')

print('Olá Usuário..!!'.center(100," "))

numero = int(input('Informe um número inteiro: '))
print()
resto = int(numero % 2) # se resto = 0 é número par e se resto = 1 o número é ímpar
"""
    se número = 6, o resto é 6/2 que é = 3, ou seja, resto = 0
    se número = 9, o resto é 9/2 que é = 4,5, ou seja, resto = 1
"""

if (resto == 0):
    print(f'O número {numero} é: PAR') #o "f" significa string formatada
else:
    print(f'O número {numero} é: ÍMPAR')

print()
print('xXx'.center(100,"*"))
print('Final do Algorítimo...!!!'.center(100," "))
print('sSs'.center(100,"-"))
print()
print('T C H A U ! ! !'.center(100," "))