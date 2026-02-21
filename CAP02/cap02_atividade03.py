import os
os.system('cls')

nomeCompleto = input('Informe seu nome completo.: ')

tamanho = len(nomeCompleto)

print('1. A quantidade de caracteres de', nomeCompleto,' é.: ',len(nomeCompleto))

print('2. Nome em maiúsculo.:', nomeCompleto.upper()) # converte em maiúscula
print('3. Nome em minúscula.:', nomeCompleto.lower()) # converte em minúscula
print('4. Converte a primeira letra em maiúscula.:', nomeCompleto.capitalize()) # converte primeira letra (só primeira letra da frase) em maiúscula

espaco = nomeCompleto.find(' ')
print('O final da primeira palavra é a posição.: ',espaco)
print('')
nome = nomeCompleto[0:espaco]
restoNome = nomeCompleto[espaco+1:tamanho]
#print('5. Retorna a palavra separada por espaços, primeira palavra.:', nomeCompleto[0:espaco]) 
print('5. Retorna a palavra separada por espaços, primeira palavra.:', nome) 
print('')
#método para substituir todos os espaços
print('6. Nome sem espaços.: ', nomeCompleto.replace(' ',''))
#esses métodos podem ser aplicados junto os inputs
print('')
print(restoNome)
#proxEsp = restoNome.find(' ')
proxEsp = nomeCompleto[espaco+1:tamanho].find(' ')
print('O final da primeira palavra é a posição.: ',proxEsp)
#método para verificar se tem somente letras
somenteLetras = nomeCompleto.replace(' ','')
print('7. Tem somente letras.: ',somenteLetras.isalpha())
#método para verificar se tem letras e números
print('8. É alfanumérico? Tem letras ou números.: ',nomeCompleto.isalnum())

#método para separar as palavras por espaços
listaPalavras = nomeCompleto.split()
#print('9. as palavras acada espaço em branco.: ', nomeCompleto.split())
print('9. Quebra as palavras a cada espaço em branco.: ', listaPalavras)

# método para centralizar o texto em 80 colunas

print('10. Centraliza o nome entre uma quantidade de caracteres <*>')
print(nomeCompleto.center(100,"*"))





