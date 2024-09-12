from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        seat_layout = QGridLayout()

        self.seat_buttons = []

        for i in range(9):
            for j in range(9):
                button = QPushButton()
                button.setStyleSheet('background-color: green')
                button.clicked.connect(self.toggle_color)
                seat_layout.addWidget(button, i, j)
                self.seat_buttons.append(button)

        self.layout.addLayout(seat_layout)

        self.ocupados_label = QLabel('Asientos Ocupados: 0')
        self.ocupados_label.setStyleSheet('color: red')
        self.layout.addWidget(self.ocupados_label)

        self.disponibles_label = QLabel('Asientos Libres: 81')
        self.disponibles_label.setStyleSheet('color: green')
        self.layout.addWidget(self.disponibles_label)

        self.recaudacion_label = QLabel('Recaudación Total: €0')
        self.recaudacion_label.setStyleSheet('color: blue')
        self.layout.addWidget(self.recaudacion_label)

        self.setLayout(self.layout)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Ejercicio 2 Examen')
        self.show()

    def toggle_color(self):
        sender = self.sender()

        current_color = sender.styleSheet()

        if 'green' in current_color:
            sender.setStyleSheet('background-color: red')
            self.update_labels(1)
        else:
            sender.setStyleSheet('background-color: green')
            self.update_labels(-1)

    def update_labels(self, change):
        sitiosocupados = sum('red' in button.styleSheet() for button in self.seat_buttons)
        sitiosdisponibles = 81 - sitiosocupados
        recaudacion = sitiosocupados * 7.5

        self.ocupados_label.setText(f'Asientos Ocupados: {sitiosocupados}')
        self.disponibles_label.setText(f'Asientos Libres: {sitiosdisponibles}')
        self.recaudacion_label.setText(f'Recaudación Total: €{recaudacion}')

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    app.exec_()
