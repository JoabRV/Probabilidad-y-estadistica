import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from calculadora import Calculadora

class CalculadoraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.calculadora = Calculadora()

        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.resultado = QLineEdit()
        self.layout.addWidget(self.resultado)

        self.crear_botones()

        self.setLayout(self.layout)

    def crear_botones(self):
        operaciones = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', 'C', '0', '=', '/']
        for texto in operaciones:
            boton = QPushButton(texto)
            boton.clicked.connect(self.on_click)
            self.layout.addWidget(boton)

    def on_click(self):
        boton = self.sender().text()
        if boton in '0123456789':
            self.resultado.setText(self.resultado.text() + boton)
        elif boton in '+-*/':
            self.operador = boton
            self.num1 = float(self.resultado.text())
            self.resultado.clear()
        elif boton == '=':
            self.num2 = float(self.resultado.text())
            if self.operador == '+':
                self.resultado.setText(str(self.calculadora.suma(self.num1, self.num2)))
            elif self.operador == '-':
                self.resultado.setText(str(self.calculadora.resta(self.num1, self.num2)))
            elif self.operador == '*':
                self.resultado.setText(str(self.calculadora.multiplicacion(self.num1, self.num2)))
            elif self.operador == '/':
                self.resultado.setText(str(self.calculadora.division(self.num1, self.num2)))
        elif boton == 'C':
            self.resultado.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraApp()
    window.show()
    sys.exit(app.exec_())
