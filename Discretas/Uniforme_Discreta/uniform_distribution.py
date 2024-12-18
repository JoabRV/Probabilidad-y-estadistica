# uniform_distribution.py

class UniformDiscreteDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if a > b:
            raise ValueError("'a' no puede ser mayor que 'b'.")

    def calculate_probability(self, value):
        """Calcula la probabilidad de que un valor esté en el rango [a, b]."""
        if self.a <= value <= self.b:
            probability = 1 / (self.b - self.a + 1)
            return probability
        else:
            raise ValueError(f"El valor {value} no está dentro del rango [{self.a}, {self.b}].")
