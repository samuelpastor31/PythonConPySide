import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog

class FontDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplicación con dialogos')
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton('Haz click para que el dialogo aparezca', self)
        self.button.setGeometry(0, 0, self.width(), self.height())
        self.button.clicked.connect(self.showFontDialog)

    def showFontDialog(self):
        font_dialog = QFontDialog(self.button.font())
        font_dialog.setWindowTitle("Selecciona una Font")

        if font_dialog.exec_() == QFontDialog.Accepted:
            selected_font = font_dialog.selectedFont()
            self.button.setFont(selected_font)
            self.button.setText('Text del Botó amb Font Personalitzada')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    font_dialog_example = FontDialogExample()
    font_dialog_example.show()
    sys.exit(app.exec_())