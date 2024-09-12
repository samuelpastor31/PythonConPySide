from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLineEdit, QSpinBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor  # nuevo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow("Nombre", QLineEdit("Hector"))
        formulario.addRow("Email", QLineEdit(text="hola@ejemplo.com"))
        formulario.addRow("Edad", QSpinBox(value=32))
        formulario.addRow("Samuel", QLineEdit())

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()

    # creamos nuestra paleta de colores
    paleta = QPalette()
    paleta.setColor(QPalette.Window, QColor(51, 51, 51))
    paleta.setColor(QPalette.WindowText, QColor(235, 235, 235))
    paleta.setColor(QPalette.Highlight, QColor(255, 0, 0))

    # activamos la paleta en la aplicación
    app.setPalette(paleta)

    window = MainWindow()
    window.show()
    app.exec_()