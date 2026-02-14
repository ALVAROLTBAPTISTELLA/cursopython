"""
  Cap04 - Atividade 01
  Tabuada (SIMPLES)

  Objetivos:
  Nesta atividade você vai montar uma Tabuada usando a estrutura de Loop do For e range.

  Comandos utilizados:
  Comandos for e range
 """

from os import system, name
system('cls') if (name == 'nt') else system('clear')

print('='.center(200,"="))
print(' T.A.B.U.A.D.A  S.I.M.P.L.E.S '.center(200,"."))
print('='.center(200,"="))

tabuada = int(input('Informe o multiplicador da tabuada desejada.: '))
print('')
titulo = f' T.A.B.U.A.D.O  D.O  N.Ú.M.E.R.O  "{tabuada}" '
#print(f' T.A.B.U.A.D.O  D.O  N.Ú.M.E.R.O  "{tabuada}" ')
print(''.center(len(titulo),"-"))
print(titulo)
print(''.center(len(titulo),"-"))
for seq in range(1,11):
    print(f'{tabuada} X {seq} = {tabuada*seq}')