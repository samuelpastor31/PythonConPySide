from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QWidget)


class Caja(QPushButton):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.setCheckable(True)
        self.setStyleSheet(f"background-color: {'green'};")
        self.clicked.connect(self.cambio_color)

    def cambio_color(self, estado):
        color = 'red' if estado else 'green'
        boton_pulsado = self.sender()
        boton_pulsado.setStyleSheet(f"background-color: {color};")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.construir_layout()

    def construir_layout(self):
        hlayout = QHBoxLayout()
        cantidad_botones = 4
        contador = 1
        for a in range(cantidad_botones):
            hlayout.addWidget(Caja(f"botón {contador}"))
            contador += 1

        hlayout.setContentsMargins(3, 3, 3, 3)
        hlayout.setSpacing(3)

        h_group_box = QGroupBox("Horizontal layout")
        h_group_box.setLayout(hlayout)

        widget = QWidget()
        widget_layout = QVBoxLayout()
        widget_layout.addWidget(h_group_box)
        widget.setLayout(widget_layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()