"""
  Cap03 - Atividade Extra
  Calcular IMC

  Objetivos:
  Nesta atividade você vai calcular o IMC a partir de um peso e uma 
  altura, usará a comando if para mostrar o resultado do calculo do IMC.
    Ex: IMC = 70 kg / (1,60 m x 1,60 m) = 70 kg / 2,56 m² = 27,3 
        IMC <18,5kg/m2 - baixo peso
        IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
        IMC ≥25 até 29,9kg/m2 - sobrepeso
        IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1
        IMC >35kg/m2 até 39,9kg/m2 - obesidade grau 2
        IMC > 40kg/m2 - obesidade extrema
  Comandos utilizados:
  Variáveis, if / elif / else
"""

#import os
#os.system('cls')

from os import system, name
system('cls') if (name == 'nt') else system('clear')


print(' CALCULADORA DE IMC '.center(200,"*"))
print('='.center(200,"="))
print('Olá usuário'.center(200," "))
print()
print('Nesta aplicação calcularemos o IMC a partir do peso e da altura'.center(200," "))
print('***'.center(200,"*"))
print()
#peso = float(input('Informe o peso.: ') if ('peso' in globals()) else 0)
#altura = float(input('Agora informe a altura.: ') if ('altura' in globals()) else 0)

peso = float(input('Informe o peso em Kg.: '))
altura = float(input('Agora informe a altura em metros (9,99).: '))

print()
print('R E S U L T A D O'.center(200,"="))
print()
#imc = peso / (altura*altura)
imc = peso / (altura**2) if ('peso' in globals()) else 0
if (imc < 18.5):
    msg = 'BAIXO PESO'
elif (imc >18.5 and imc <24.5):
    msg = 'PESO ADEQUADO - eutrofia'
elif (imc >= 25 and imc < 29.9):
    msg = 'SOBREPESO'
elif (imc > 30 and imc < 34.9):
    msg  = 'OBESIDADE GRAU 1'
elif (imc >35 and imc < 39.9):
    msg = 'OBESIDADE GRRAU 2'
elif (imc > 40):
    msg = 'OBESIDADE EXTREMA'
else:
    peso = 0
    altura = 0
    print()

print(f'O IMC calculado foi de {imc:.4f}kg/a2, resultando em {msg}'.center(200," ") if ('imc' in globals()) else 'NÃO FORAM INFORMADOS PARÂMETROS..!!!'.center(200," "))


