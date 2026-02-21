"""
    Python = "Lista" ou "Tupla"
    Outras = "Array" ou "Vetor"

             0|-5    1|-4     2|-3       3|-2     4|-1
    nomes = ["José", "Maria", "Joaquim", "Joana", "João"]
    print(nomes[2])  # Joaquim
    print(nomes[1])  # Maria
    print(nomes[-1]) # João

"""
"""
  Cap05 - Atividade 01

  Número por Extenso

  Objetivos:
  Nesta atividade você vai escrever um número por extenso, para isto usará uma tupla. 
  A tupla é um array que contém dados que não podem ser alterados.

  Comandos utilizados:
  Tupla, operadores / e %

  Para atualizar o projeto no GITHUB:

  git add .
  git commit -m "comentário sobre a atualização"
  git push -u origin main

  origin é a URL "github.com/alvaroltbaptistella..."
  main é a BRANCH
"""
# tupla é criada com () e não pode ter seus dados alterados
# lista é criada com [] e pode ter seus dados alterados

from os import system, name
system('cls') if (name == 'nt') else system('clear')

unidades = ('zero', 'um', 'dois', 'três', 'quatro',  'cinco', 'seis', 'sete', 'oito', 'nove', )
dezenas = ('dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',)
rasos = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', ) # as duas primeiras posições equivalem à unidades e à dezenas

print(' TRANFORMAR NÚMERO POR EXTENSO '.center(200,"="))
numero = int(input("Informe um número entre 0 e 99 para ser convertido em texto: "))
print('')

if numero < 10:
    numTexto = unidades[numero]
elif numero < 20:
    numTexto = dezenas[numero-10]
elif numero < 99:
    u = numero % 10
    d = int(numero/10)
    #numTexto = rasos[d], ' e ', unidades[u]
    #numTexto = f'{rasos[d]} e  {unidades[u]}'

    numTexto = rasos[d]
    if u > 0:
        numTexto += f' e {unidades[u]}'
else:
    numTexto = f'O valor {numero} é inválido, tente mais tarde novamente.!!!'

maiuscula = numTexto.upper()
print("*".center(200,"*"))
print('')
print(maiuscula.center(200," "))
print('')
print("*".center(200,"*"))
print(u)
print(d)