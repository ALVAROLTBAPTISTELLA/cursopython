"""
  Cap07 - Atividade 02
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""
from cap07_atividade02_classe import Recibo
from os import system, name

def limparTela():
    system('cls') if (name == 'nt') else system('clear')

def menucabecalho(nome):
    print("* * * * * *".center(200,"="))
    print(f' * * -- {nome} -- * * '.center(200," ")) #substituir pelo nome da atividade
    print('='.center(200,"="))
    print()

#system('cls') if(name == 'nt') else system('clear')
    
limparTela()
input()

atividade = input('Informe o nome da atividade.: ')
limparTela()
menucabecalho(atividade)

nome = input('Informe a o nome do cliente.: ') #recebe o nome para criação da classe
v = float(input('Informe o valor do Recibo.: '))
dados = Recibo(nome) # instancia a classe recibo
#valor = float(input('Informe o valor: ')) # entrada do valor para conversão

#d = input('Informe a descrição do serviço executado.: ')
#dados.descricao(d)

dados.descricao(input('Informe a descricao do serviço executado.: ')) # como chamar a classe sem o decorador @
dados.valor = v # como chamar a função da classe com o decorador @ setter

limparTela()
menucabecalho(atividade)
print(dados)

