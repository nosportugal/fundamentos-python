# def soma(x, y):
#     resultado_soma = x + y
#     print("soma: ", resultado_soma)
#     return resultado_soma, resultado_soma * 2, 10


# resultado, resultado_dobrado, numero = soma(10, 10)
# print(resultado, resultado_dobrado, numero)


# class Calculadora:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def soma(self):
#         return self.x + self.y


# calculadora = Calculadora(10, 5)
# print(calculadora.soma())
# print(calculadora.x, calculadora.y)

# class Calculadora:

#     def soma(self, x, y):
#         return x + y

#     def subtracao(self, x, y):
#         return x - y   


# calculadora = Calculadora()
# print(calculadora.soma(10, 5))
# print(calculadora.subtracao(10, 5))

# soma = lambda x, y: x + y
# print(soma(10, 5))


class Calculadora:
    def _soma(self, x, y):
        return x + y

    def _subtracao(self, x, y):
        return x - y

    def calculo(self, operacao, x, y):
        if operacao == "soma":
            return self._soma(x, y)
        elif operacao == "subtracao":
            return self._subtracao(x, y)


resultado = Calculadora().calculo("soma", 10, 20)
print(resultado)


