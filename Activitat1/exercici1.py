from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QHBoxLayout, QWidget
from PySide6.QtCore import Slot,QSize

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercici 1")
        layout = QHBoxLayout()

        texto = QLineEdit()
        texto.setMaxLength(5)
        texto.textChanged.connect(self.update_label)
        texto.setFixedSize(QSize(50, 30))

        self.marco = QLabel()
        self.marco.setFixedSize(QSize(50, 30))

        layout.addWidget(texto)
        layout.addWidget(self.marco)
        self.setLayout(layout)

    @Slot()
    def update_label(self, text):
        self.marco.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()