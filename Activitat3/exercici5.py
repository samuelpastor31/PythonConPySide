from PySide6.QtWidgets import (
    QApplication, QTextEdit, QMainWindow, QGroupBox, QGridLayout, QDialogButtonBox, QHBoxLayout, QVBoxLayout, QPushButton, QWidget,
    QLineEdit, QLabel)
from PySide6.QtGui import QAction


class Box(QPushButton):
    def __init__(self, text):
        super().__init__(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Layouts")
        self.resize(400, 400)
        self.create_menu()
        self.create_layouts()
      

    def create_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&File")
        self.action_exit = QAction("&Exit", self)
        self.action_exit.triggered.connect(self.close)
        menu_archivo.addAction(self.action_exit)

    def create_layouts(self):
        button_layout = QHBoxLayout()
        quantity_buttons = 4
        for a in range(quantity_buttons):
            button_layout.addWidget(Box("Botón " + str(a + 1)))

        group_box_buttons = QGroupBox("Horizontal layout")
        group_box_buttons.setLayout(button_layout)

        label_line1 = QLabel("Línea 1")
        label_line2 = QLabel("Línea 2")
        
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()

        text_edit = QTextEdit()
        text_edit.setText("Aço es un QTextEdit")

        grid_layout = QGridLayout()
        grid_layout.addWidget(label_line1, 0, 0)
        grid_layout.addWidget(line_edit1, 0, 1)
        grid_layout.addWidget(label_line2, 1, 0)
        grid_layout.addWidget(line_edit2, 1, 1)
        grid_layout.addWidget(text_edit, 0, 2, 2, 1)

        group_box_grid = QGroupBox("Grid layout")
        group_box_grid.setLayout(grid_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box_buttons)
        main_layout.addWidget(group_box_grid)
        main_layout.addWidget(button_box)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()