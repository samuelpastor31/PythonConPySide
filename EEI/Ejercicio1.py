import sys
from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, QMainWindow, QMenuBar, QMenu, QDialogButtonBox, QGroupBox, QComboBox
from PySide6.QtGui import QAction

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Botón 1')
        btn2 = QPushButton('Botón 2')
        btn3 = QPushButton('Botón 3')
        btn4 = QPushButton('Botón 4')

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(btn1)
        hbox_buttons.addWidget(btn2)
        hbox_buttons.addWidget(btn3)
        hbox_buttons.addWidget(btn4)

        groupbox_buttons = QGroupBox('Botones')
        groupbox_buttons.setLayout(hbox_buttons)

        dialogButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        gridWidget = QWidget()
        gridLayout = QGridLayout(gridWidget)

        groupbox_form_layout = QGroupBox('Grid Layout')
        form_layout = QFormLayout(groupbox_form_layout)

        label_line1 = QLabel('Línea 1')
        label_line1.setStyleSheet('font-size: 12pt;')
        text_edit_1 = QTextEdit()
        text_edit_1.setMaximumHeight(30)
        form_layout.addRow(label_line1, text_edit_1)

        label_line2 = QLabel('Línea 2')
        label_line2.setStyleSheet('font-size: 12pt;')
        text_edit_2 = QTextEdit()
        text_edit_2.setMaximumHeight(30)
        form_layout.addRow(label_line2, text_edit_2)

        label_line3 = QLabel('Línea 3')
        label_line3.setStyleSheet('font-size: 12pt;')
        text_edit_3 = QTextEdit()
        text_edit_3.setMaximumHeight(30)
        form_layout.addRow(label_line3, text_edit_3)

        gridLayout.addWidget(groupbox_buttons, 0, 0, 1, 3)
        gridLayout.addWidget(groupbox_form_layout, 1, 0, 1, 1)

        groupbox_below = QGroupBox('Form layout')
        form_layout_below = QFormLayout(groupbox_below)

        label_line4 = QLabel('Línea 1')
        label_line4.setStyleSheet('font-size: 12pt;')
        text_edit_4 = QTextEdit()
        text_edit_4.setMaximumHeight(30)
        form_layout_below.addRow(label_line4, text_edit_4)

        label_line5 = QLabel('Línea 2 ')
        label_line5.setStyleSheet('font-size: 12pt;')
        combo_box_below = QComboBox()
        combo_box_below.addItems([''])
        form_layout_below.addRow(label_line5, combo_box_below)

        label_line6 = QLabel('Línea 3')
        label_line6.setStyleSheet('font-size: 12pt;')
        text_edit_6 = QTextEdit()
        text_edit_6.setMaximumHeight(30)
        form_layout_below.addRow(label_line6, text_edit_6)

        gridLayout.addWidget(groupbox_below, 2, 0, 1, 3)

        groupbox_paragraph = QGroupBox('')
        vbox_paragraph = QVBoxLayout(groupbox_paragraph)
        paragraph_text_edit = QTextEdit()
        vbox_paragraph.addWidget(paragraph_text_edit)

        gridLayout.addWidget(groupbox_paragraph, 1, 1, 1, 2)
        gridLayout.addWidget(dialogButtonBox, 3, 0, 1, 3)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        central_widget = QWidget()
        central_widget.setLayout(gridLayout)
        self.setCentralWidget(central_widget)

        self.setGeometry(300, 300, 1000, 400)
        self.setWindowTitle('Ejercicio 1 Examen')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    sys.exit(app.exec_())