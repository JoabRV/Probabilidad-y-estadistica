# bernoulli_distribution.py

class BernoulliDistribution:
    def __init__(self, p):
        if not (0 <= p <= 1):
            raise ValueError("La probabilidad p debe estar entre 0 y 1.")
        self.p = p  # Probabilidad de éxito (valor entre 0 y 1)

    def calculate_probability(self, outcome):
        """Calcula la probabilidad de un resultado dado (0 o 1)."""
        if outcome == 1:
            return self.p
        elif outcome == 0:
            return 1 - self.p
        else:
            raise ValueError("El valor debe ser 0 o 1.")
