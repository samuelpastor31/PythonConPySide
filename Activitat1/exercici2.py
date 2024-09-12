from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QCheckBox, QGroupBox
from PySide6.QtCore import Slot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de Checkboxs")

        layout = QVBoxLayout()

        group_box = QGroupBox("Exclusive Radio Button")
        group_layout = QVBoxLayout()

        self.checkbox1 = QCheckBox("Primer checkbox")
        self.checkbox2 = QCheckBox("Segundo checkbox")
        self.checkbox3 = QCheckBox("Tercer checkbox")

        self.checkbox1.stateChanged.connect(self.mostrar_mensaje)
        self.checkbox2.stateChanged.connect(self.mostrar_mensaje)
        self.checkbox3.stateChanged.connect(self.mostrar_mensaje)

        group_layout.addWidget(self.checkbox1)
        group_layout.addWidget(self.checkbox2)
        group_layout.addWidget(self.checkbox3)

        group_box.setLayout(group_layout)
        layout.addWidget(group_box)

        self.setLayout(layout)

    @Slot(int)
    def mostrar_mensaje(self, state):
        sender = self.sender()
        if state == 2: 
            print(f"El checkbox {sender.text()} ha sido marcado")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()