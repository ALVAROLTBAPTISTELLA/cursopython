class Calculadora:
    # instanciar a classe
    def __init__(self, valor1, valor2): # -> None:
        self.__valor1 = valor1 # __ é para proteger o atributo da classe
        self.__valor2 = valor2

    # métodos da classe
    def soma(self):
        return self.__valor1+self.__valor2
    def sub(self):
        return self.__valor1 - self.__valor2
    def mult(self):
        return self.__valor1 * self.__valor2
    def div(self):
        return self.__valor1 / self.__valor2


