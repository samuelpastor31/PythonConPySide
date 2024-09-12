from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Refrans")
        self.button = QPushButton("Refrà aleatori")
        self.button.clicked.connect(self.mostrar_refran)
        self.setCentralWidget(self.button)
        self.refranes = [
            "Haz el bien sin mirar a quien",
            "Más vale prevenir que curar",
            "A mal tiempo, buena cara",
            "Quien tiene un amigo tiene un tesoro",
            "La avaricia rompe el saco",
            "De los errores se aprende"
        ]

    def mostrar_refran(self):
        refran = choice(self.refranes)
        self.setWindowTitle(refran)
        if refran == "De los errores se aprende":
            self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()