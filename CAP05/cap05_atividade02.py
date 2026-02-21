"""
  Cap05 - Atividade 02

  Jogo: Papel, pedra e Tesoura

  Objetivos:
  Nesta atividade você vai criar um jogo usando tupla e tupla multi-dimensional.

  Comandos utilizados:
  Tupla, Tupla Multi-Dimensional, biblioteca random e randint
"""

from os import system, name
system('cls') if (name == 'nt') else system('clear')

# biblioteca random
import random

opcao = 's'
#print(" JOGO: PEDRA PAPEL TESOURA ".center(200,'='))
while opcao.upper()=='S':
    system('cls') if (name == 'nt') else system('clear')
    print(" JOGO: PEDRA PAPEL TESOURA ".center(200,'='))
    opcoes = ('Pedra', 'Papel', 'Tesoura')
    print(' Suas opções são: ')
    print('')
    #print("Escolha sua jogada.: ")
    for i, elemento in enumerate(opcoes):
        print(f'{i+1} - {elemento}')
        print('')
    jogador = int(input("Escolha sua jogada.: "))-1
    print('')
    cpu = random.randint(0,2)
    #escCpu = cpu+1

    jM = "parabéns, você venceu.!!! :)"
    eM = "Deu empate, só peerdeu tempo /:"
    cpuM = "Deu RED. A CPU venceu :("

    resultado = (
                (eM, jM, cpuM),
                (cpuM, eM, jM),
                (jM, cpuM, eM),
                )
    
    print(f'Você escolheu...: {(jogador)+1} - {opcoes[jogador]}')
    print(f'A CPU escolheu..: {(cpu)+1} - {opcoes[cpu]}')
    print('')
    print(resultado[cpu][jogador])
    print('')
    opcao = input("Digite S para continuar ou qualquer tecla para finalizar.: ")