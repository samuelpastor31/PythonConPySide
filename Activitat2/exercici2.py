from PySide6.QtWidgets import (
QGridLayout,QPushButton,QApplication, QMainWindow, QWidget
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        layout = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout)
        self.setCentralWidget(componente_principal)

        layout.addWidget(QPushButton("Botó 1"),0,0)
        layout.addWidget(QPushButton("Botó 2"),0,1)
        layout.addWidget(QPushButton("Botó 3"),0,2)
        layout.addWidget(QPushButton("Botó 4"),0,3)
    

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()