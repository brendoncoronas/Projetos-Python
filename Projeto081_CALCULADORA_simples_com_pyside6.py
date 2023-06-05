import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QVBoxLayout, QWidget)


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.input_label = QLabel("Digite a expressão")
        self.input_lineedit = QLineEdit()
        self.result_label = QLabel("Resultado")

        self.calculate_button = QPushButton("Calcular"
        self.calculate_button.clicked.connect(self.calculate_result

        layout.addWidget(self.input_label
        layout.addWidget(self.input_lineedit
        layout.addWidget(self.result_label
        layout.addWidget(self.calculate_button

        central_widget = QWidget(
        central_widget.setLayout(layout
        self.setCentralWidget(central_widget

    def calculate_result(self
        expression = self.input_lineedit.text(
        try
            result = eval(expression
            self.result_label.setText(f"Resultado: {result
        except Exception as e
            self.result_label.setText(f"Erro: {str(e


if __name__ == "__main__
    app = QApplication(sys.argv
    calculator = CalculatorApp(
    calculator.show(
    sys.exit(app.exec(
