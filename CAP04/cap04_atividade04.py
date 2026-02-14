"""
  Cap04 - Atividade 03
  Verificar Número Primo

  Objetivos:
  Nesta atividade você vai verificar se um número é primo ou não e ainda indicar quem é o menor divisor deste número, usando o WHILE para o realizar o loop.

  Comandos utilizados:
  Comando f com variável de substituição, comando while e break e if ternário
"""

from os import system, name
system('cls') if (name == 'nt') else system('clear')

numero = int(input('Informe um número inteiro.: '))
i = 2
divisor = 0
tipo = 'O número deve ser maior que 2'

#loop enquanto satisfizer a condição true/false
while (i<numero): #teste boolean (true/false)
    tipo = 'O número é PRIMO'
    x = numero % i
    # se resto = 0 não é primo
    if (x==0):
        divisor = i
        tipo = 'O número NÃO é PRIMO'
        break #encerra o loop
    i += 1
print(tipo)
print(f'O menor divisor é.: {divisor}' if (divisor > 0) else '')