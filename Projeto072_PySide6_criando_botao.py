# faça um projeto com Py
import sys

# QApplication - é responsavel por gerenciar a nossa aplicação e tbm
# e tbm nao exibe nada na tela
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)  # type: ignore

botao = QPushButton('texto do botao')
botao.setStyleSheet('font-size: 20px;')
botao.show()  # adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('botao 2')
botao2.setStyleSheet('font-size: 20px;')


central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)

central_widget.show()  # central_widget entre na hierarquia e mostre sua janela

# o loop da aplicação:

app.exec()
