class Calculadora:
    def __init__(self):
        self.resultado = 0

    def suma(self, a, b):
        self.resultado = a + b
        return self.resultado

    def resta(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicacion(self, a, b):
        self.resultado = a * b
        return self.resultado

    def division(self, a, b):
        if b != 0:
            self.resultado = a / b
        else:
            self.resultado = "Error: Division por 0"
        return self.resultado

