import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

# parent - um elemento que é pai desse outro elemento
# nesse super - caso eu recebe parent eu qro passar ele la para dentro


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # botao1
        self.botao1 = self.Make_Button('texto do botão1')
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.central_widget = QWidget() # widget generico

        # funcionalidades
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        self.botao2 = self.Make_Button('botão 2')
        self.botao3 = self.Make_Button('botão 3')

        self.grid_layout = QGridLayout()  # layout para colocar outro widget
        # dentro do widget generico

        # aqui fazemos a ligação entre eles, para
        self.central_widget.setLayout(self.grid_layout
        # podermos adicionar os widgets

        self.grid_layout.addWidget(self.botao1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)
        # falamos p o botao3 se expandir na mesma linha, porem se expandir
        # 2 colunas

        # status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('mostra mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('primeira ação')
        self.primeira_acao.triggered.connect(self.muda_mendagem_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(
            self.segunda_acao_marcada)  # type: ignore
        # pq na outra eu coloquei uma lambda e nessa não?
        # pq eu li na documentação que ja é automatico eu receber
        # checked(argumento da func) no 'outro_slot'

        self.segunda_action.hovered.connect(
            self.segunda_acao_marcada)  # type: ignore
        # estamos recebendo o 'segunda_action' por estamos implementando outra
        # funcionalidade nela tbm (de passar o mouse em cima e dizer se ela
        # esta false ou true, depois que clicarmos o resultado muda)

    @Slot()  # type: ignore
    def muda_mendagem_status_bar(self, status_bar):
        status_bar.showMessage('o meu slot foi executado')

    @Slot()  # type: ignore
    def segunda_acao_marcada(self):
        print('esta marcado?', self.segunda_action.isChecked())

    def Make_Button(self, text):
        bnt = QPushButton(text)
        bnt.setStyleSheet('font-size: 80px
        return bnt


if __name__ == '__main__
    app = QApplication(sys.argv
    window = MyWindow(  # estamos usando agora o QMainWindow pois tem mais
    window.show(
    app.exec(    # executa o loop da aplicação
