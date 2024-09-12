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

        self.red_label = QLabel('Seients ocupats')
        self.red_label.setStyleSheet('color: red')
        self.layout.addWidget(self.red_label)

        self.green_label = QLabel('Seients lliures')
        self.green_label.setStyleSheet('color: green')
        self.layout.addWidget(self.green_label)

        self.money_label = QLabel('Recaptació total')
        self.money_label.setStyleSheet('color: blue')
        self.layout.addWidget(self.money_label)

        self.setLayout(self.layout)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Cines Batoi')
        self.show()

    def toggle_color(self):
        sender = self.sender()

        current_color = sender.styleSheet()

        if 'red' in current_color:
            sender.setStyleSheet('background-color: green')
            self.update_labels(-1)
        else:
            sender.setStyleSheet('background-color: red')
            self.update_labels(1)

    def update_labels(self, change):
        readseats = sum('red' in button.styleSheet() for button in self.seat_buttons)
        greenseats = 81 - readseats
        money = readseats * 7,5

        self.red_label.setText(f'Seients ocupats {readseats}')
        self.green_label.setText(f'Seients lliures {greenseats}')
        self.money_label.setText(f'Recaptació Total = {money} €')

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    app.exec_()
