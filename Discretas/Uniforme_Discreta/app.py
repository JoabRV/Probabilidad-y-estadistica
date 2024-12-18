# app.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from uniform_distribution import UniformDiscreteDistribution


class UniformDiscreteDistributionUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Distribución Uniforme Discreta")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Layout de los campos de formulario
        form_layout = QFormLayout()

        # Campos de entrada para el rango
        self.a_input = QLineEdit(self)
        self.b_input = QLineEdit(self)

        # Campo para el valor a evaluar
        self.value_input = QLineEdit(self)

        # Campo de salida para la probabilidad
        self.result_label = QLabel("Probabilidad: ", self)

        form_layout.addRow("Valor mínimo (a):", self.a_input)
        form_layout.addRow("Valor máximo (b):", self.b_input)
        form_layout.addRow("Valor para calcular probabilidad:", self.value_input)

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
            a = int(self.a_input.text())
            b = int(self.b_input.text())
            value = int(self.value_input.text())

            # Crear instancia de la clase de distribución
            dist = UniformDiscreteDistribution(a, b)

            # Calcular la probabilidad
            probability = dist.calculate_probability(value)
            self.result_label.setText(f"Probabilidad de {value}: {probability:.4f}")

        except ValueError as e:
            self.result_label.setText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UniformDiscreteDistributionUI()
    window.show()
    sys.exit(app.exec_())
