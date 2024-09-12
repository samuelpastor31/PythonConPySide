import sys
from PySide6.QtWidgets import QDoubleSpinBox,QSpinBox,QApplication, QWidget, QLabel, QLineEdit, QGridLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Ejemplo de QLineEdit al lado de un texto")

layout = QGridLayout()

label = QLabel("Texto:")
edit = QLineEdit()
label2 = QLabel("Enter:")
spin = QSpinBox()
label3 = QLabel("Decimal:")
decimal = QDoubleSpinBox()

layout.addWidget(label, 0, 0)
layout.addWidget(edit, 0, 1)
layout.addWidget(label2, 1, 0)
layout.addWidget(spin, 1, 1)
layout.addWidget(label3, 2, 0)
layout.addWidget(decimal, 2, 1)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
