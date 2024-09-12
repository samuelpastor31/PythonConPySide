import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplicación con dialogos')
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton('Haz click para que el dialogo aparezca', self)
        self.button.setGeometry(0, 0, self.width(), self.height())
        self.button.clicked.connect(self.showColorDialog)

    def showColorDialog(self):
        color_dialog = QColorDialog(self)

        if color_dialog.exec_():
            selected_color = color_dialog.selectedColor()
            self.button.setStyleSheet(f'background-color: {selected_color.name()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())