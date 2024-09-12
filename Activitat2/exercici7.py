from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PySide6.QtGui import QColor

class ChessboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Configurar el espaciado entre widgets a 0
        central_widget.setLayout(grid_layout)

        # Crear el tablero de ajedrez con QLabel blanco y negro
        for i in range(8):
            for j in range(8):
                label = QLabel()
                label.setFixedSize(50, 50)  # Tamaño fijo para cada cuadrado
                if (i + j) % 2 == 0:
                    label.setAutoFillBackground(True)
                    palette = label.palette()
                    palette.setColor(label.backgroundRole(), QColor("white"))
                    label.setPalette(palette)
                else:
                    label.setAutoFillBackground(True)
                    palette = label.palette()
                    palette.setColor(label.backgroundRole(), QColor("black"))
                    label.setPalette(palette)
                grid_layout.addWidget(label, i, j)

if __name__ == "__main__":
    app = QApplication([])
    window = ChessboardWindow()
    window.show()
    app.exec()
