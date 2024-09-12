import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QGroupBox, QVBoxLayout, QCheckBox)
from PySide6.QtCore import Qt

class CheckboxExample(QMainWindow):
    def __init__(self):
        super().__init__()

        checkbox_group = QGroupBox("Exclusive Radio Buttons")
        layout = QVBoxLayout()

        checkbox1 = QCheckBox("Primer checkbox")
        checkbox2 = QCheckBox("Segundo checkbox")
        checkbox3 = QCheckBox("Tercer checkbox")

        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)
        layout.addWidget(checkbox3)

        checkbox_group.setLayout(layout)
        self.setCentralWidget(checkbox_group)

if __name__ == "__main__":
    app = QApplication([])
    window = CheckboxExample()
    window.show()
    sys.exit(app.exec_())