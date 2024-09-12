from PySide6.QtWidgets import (
QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        layout = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout)
        self.setCentralWidget(componente_principal)
        
        layout.addWidget(QPushButton('0,0'), 0, 0)
        layout.addWidget(QPushButton('0,1'), 0, 1)
        layout.addWidget(QPushButton('0,2'), 0, 2)
        layout.addWidget(QPushButton('0,3'), 0, 3)
# Añadimos un botón a la seguna fila que ocupe dos columnas
        layout.addWidget(QPushButton('1,0-3'), 1, 0, 1, 4)
        layout.addWidget(QPushButton('2,0-1'), 2, 0, 2,2)
        layout.addWidget(QPushButton('0,2-3'), 2, 2, 2,3)

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()