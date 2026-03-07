"""
  Cap07 - Atividade 02
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e 
  propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""

from num2words import num2words
class Recibo:
    # MÉTODO QUE INSTANCIA A CLASSE
    def __init__(self, nome):
        self.nome = nome
        self._valor = 0           #usar dois __ deixa o atributo privado, um _ protege
        self._descricao = '' 

    #método para alterar a descrição
    def descricao(self, value):
        self._descricao = value

    @property # O @ é um decorador que transforma em propriedade para consultar
    def valor(self):
        return(self._valor)
    
    # método que recebe o valor para ser alterado
    @valor.setter
    def valor(self, value):
        self._valor = value

    # método que converte para extenso  
    def extenso(self):
        vExtenso = num2words(self._valor, lang='pt-br', to= 'currency')
        return vExtenso
    
    def __str__(self):
        texto = f'Recebemos de {self.nome} a quantia de R$ {self._valor:.2f} ({self.extenso()})'
        descricao = f'\n referente a {self._descricao}' if (self._descricao!='') else ''
        dados = f'{'Recibo'.center(len(texto),"*")}\n {texto} {descricao}'
        #dados = '{}/n{}{}' .format('Recibo'.center(len(texto),"*"), texto, descricao)
        # as {} são os parâmetros dentro do format -- Recibo, texto, descrição
        return dados
    

        