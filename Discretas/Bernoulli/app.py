# app.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from bernoulli_distribution import BernoulliDistribution


class BernoulliDistributionUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Distribución Bernoulli Discreta")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Layout de los campos de formulario
        form_layout = QFormLayout()

        # Campo de entrada para la probabilidad de éxito
        self.p_input = QLineEdit(self)

        # Campo para el resultado a evaluar (0 o 1)
        self.outcome_input = QLineEdit(self)

        # Campo de salida para la probabilidad
        self.result_label = QLabel("Probabilidad: ", self)

        form_layout.addRow("Probabilidad de éxito (p):", self.p_input)
        form_layout.addRow("Resultado (0 o 1):", self.outcome_input)

        layout.addLayout(form_layout)

        # Botón para calcular la probabilidad
        self.calculate_button = QPushButton("Calcular Probabilidad", self)
        self.calculate_button.clicked.connect(self.calculate_probability)
        layout.addWidget(self.calculate_button)

        # Resultado
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_probability(self):
        # Obtener los valores de los campos de entrada
        try:
            p = float(self.p_input.text())
            outcome = int(self.outcome_input.text())

            # Crear instancia de la clase de distribución
            dist = BernoulliDistribution(p)

            # Calcular la probabilidad
            probability = dist.calculate_probability(outcome)
            self.result_label.setText(f"Probabilidad de {outcome}: {probability:.4f}")

        except ValueError as e:
            self.result_label.setText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BernoulliDistributionUI()
    window.show()
    sys.exit(app.exec_())
