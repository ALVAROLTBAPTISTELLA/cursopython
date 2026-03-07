"""
  Cap07 - Atividade 01
  Criar uma Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e 
  propriedades e como consumir esta classe.

  Comandos utilizados:
  Classe, Propriedades e Metodos de uma classe
"""

from cap07_atividade01_classe import Calculadora

from os import system, name

def limparTela():
    system('cls') if (name == 'nt') else system('clear')

def menucabecalho(nome):
    print("* * * * * *".center(200,"="))
    #print(' * * -- C A L C U L A D O R A -- * * '.center(200," ")) #substituir pelo nome da atividade
    print(f' * * -- {nome} -- * * '.center(200," ")) #substituir pelo nome da atividade
    print('='.center(200,"="))
    print()

def menuopcoes():
    print(f'''
                1 - Soma            {calc.soma()}
                2 - Subtração       {calc.sub()}
                3 - Multiplicação   {calc.mult()}
                4 - Divisão         {calc.div()}
            ''') 

atividade = "C A L C U L A D O R A"

limparTela()
menucabecalho(atividade)

from CAP07.cabecalho.cap07_atividade01 import menucabecalho

valor1 = int(input('Informe o 1º valor.: '))
valor2 = int(input('Informe o 2º valor.: '))

#construindo o objeto da classe

calc = Calculadora(valor1, valor2)

#acessar o método da classe

menuopcoes()

'''

print(f'Soma.: {calc.soma()}')
print(f'Subtração.: {calc.sub()}')
print(f'Multiplicação.: {calc.mult()}')
print(f'Divisão.: {calc.div()}')

'''