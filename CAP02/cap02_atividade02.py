"""
cálculo da área de um retângulo.

receber a entrada de dois valores correspondentes aos lados de um retângulo em cm e realizar o cálculo da área de um retângulo.
"""

print()
nome = input('Poderia informar seu nome? ')
print('Olá',nome.strip(),', vamos efetuar o cáculo da área de um retângulo.!')
print('')
print('Precisamos para isso dos valores dos lados, em centímetros e valores inteiros, Ok.!!')
print('')
#pergunta = 'Informe,', nome, 'o 1º valor.: '
#lado01 = input(pergunta)
lado01 = input('Informe o 1º valor.: ')
lado02 = input('Informe o 2º valor.: ')
#lado01 = int(lado01)
#lado02 = int(lado02)
lado01 = float(lado01)
lado02 = float(lado02)
areaTotal = lado01*lado02
print('')
print('Agora faremos os cálculos!!')
print('')
#print('A área total do retângulo é.: ',lado01*lado02,' cm²')
print('A área total do retângulo é.: ',areaTotal,' cm²')
print('')
print('Chegamos ao resultado',nome)
