"""
  Cap03 - Atividade 02
  Conversor de Medidas

  Objetivos:
  Nesta atividade você vai converter um número em centimetros para Polegada, Pé ou Jarda. 
  Será necessário usar o comando if / elif / else.

  Comandos utilizados:
  If / elif / else, formatação de números com posição de substituição {:.4f}
"""

import os
os.system('cls')

print('Olá Usuário'.center(100," "))

medidaCm = float(input('Informe a medida em centímetros..: '.center(100," ")))
print()
print('Informe como gostaria de converter esta medida'.center(100," "))
print()
print('1 - Polegada\n2 - Pé\n3 - Jarda')
#print('1 - Polegada'.center(100," "))
#print('2 - Pé'.center(100," "))
#print('3 - Jarda'.center(100," "))

print()
print('Qual sua opção.?'.center(100," "))
print()
menu = input('Opção.: '.center(100," "))
print()
if (menu == '1'):
    unidade = 'Polegada'
    resConversao = medidaCm/2.54
#    print('')
elif (menu == '2'):
        unidade = 'Pé'
        resConversao = medidaCm/30.48
#        print('')
elif (menu == '3'):
        unidade = 'Jarda'
        resConversao = medidaCm/91.44
else:
       resConversao = 0
#       print('')
#    unidade = 'I N V Á L I D A..!!!'
#    resConversao = 0
#print()
#print(f'{medidaCm} em {unidade} corresponde à: {resConversao:.4f}'.center(100," "))
       #unidade = ''
#print('Opção I N V Á L I D A . . . ! ! !'.center(100," ") if (unidade=='') else f'{medidaCm} em {unidade} corresponde à: {resConversao:.4f}'.center(100," "))
       
print('')       
print(f'{medidaCm}cm em {unidade} corresponde à: {resConversao:.4f}'.center(100," ") if ('unidade' in globals()) else 'Opção I N V Á L I D A . . . ! ! !'.center(100," "))