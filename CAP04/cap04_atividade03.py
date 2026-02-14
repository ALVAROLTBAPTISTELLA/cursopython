"""
  Cap04 - Atividade 02
  MultiTabuada

  Objetivos:
  Nesta atividade você vai construir uma multitabuada de duas maneiras, na primeira usando for e na segunda usando for aninhado

  Comandos utilizados:
   Comandos for range
"""

from os import system, name
system('cls') if (name == 'nt') else system('clear')

print('='.center(200,"="))
print(' T.A.B.U.A.D.A  M.U.L.T.I.P.L.A - 1ª forma '.center(200,"."))
print('='.center(200,"="))

#n corresponde aos número para multiplicar
#tabu corresponde ao multiplicado

for i in range(1,11):
    traco = f'{i*1:>4}| {i*2:>4}| {i*3:>4}| {i*4:>4}| {i*5:>4}| {i*6:>4}| {i*7:>4}| {i*8:>4}| {i*9:>4}| {i*10:>4}'
    print(f'{i*1:>4}| {i*2:>4}| {i*3:>4}| {i*4:>4}| {i*5:>4}| {i*6:>4}| {i*7:>4}| {i*8:>4}| {i*9:>4}| {i*10:>4}') 
    print('-'.center(len(traco),"-"))

system('cls') if (name == 'nt') else system('clear')

print('='.center(200,"="))
print(' T.A.B.U.A.D.A  M.U.L.T.I.P.L.A - 2ª forma '.center(200,"."))
print('='.center(200,"="))
print('')
print('T A B E L A  G E R A D A !!!'.center(60," "))

for  i in range(1,11):
    linha = f'|{i:>4} |'
    for ii in range(2,11):
        linha += f'{i*ii:>4} |'
    print('-'.center(len(linha),"-"))
    print(linha)  
print('-'.center(len(linha),"-"))