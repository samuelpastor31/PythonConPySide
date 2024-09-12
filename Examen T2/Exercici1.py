import sys
from PySide6.QtWidgets import QApplication,QSpinBox, QFormLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, QMainWindow, QMenuBar, QMenu, QDialogButtonBox, QGroupBox, QComboBox
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        boton1 = QPushButton('Botón 1')
        boton2 = QPushButton('Botón 2')
        boton3 = QPushButton('Botón 3')
        boton4 = QPushButton('Botón 4')

        hboxButtons = QHBoxLayout()
        hboxButtons.addWidget(boton1)
        hboxButtons.addWidget(boton2)
        hboxButtons.addWidget(boton3)
        hboxButtons.addWidget(boton4)

        groupbox_buttons = QGroupBox('Horizontal Layout')
        groupbox_buttons.setLayout(hboxButtons)

        gridWidget = QWidget()
        gridLayout = QGridLayout(gridWidget)

        groupbox_form_layout = QGroupBox('Grid Layout')
        form_layout = QFormLayout(groupbox_form_layout)

        line1 = QLabel('Línea 1')
        line1.setStyleSheet('font-size: 11pt;')
        text_edit_1 = QTextEdit()
        text_edit_1.setMaximumHeight(20)
        form_layout.addRow(line1, text_edit_1)

        line2 = QLabel('Línea 2')
        line2.setStyleSheet('font-size: 11pt;')
        text_edit_2 = QTextEdit()
        text_edit_2.setMaximumHeight(20)
        form_layout.addRow(line2, text_edit_2)

        label_line3 = QLabel('Línea 3')
        label_line3.setStyleSheet('font-size: 11pt;')
        text_edit_3 = QTextEdit()
        text_edit_3.setMaximumHeight(20)
        form_layout.addRow(label_line3, text_edit_3)

        gridLayout.addWidget(groupbox_buttons, 0, 0, 1, 3)
        gridLayout.addWidget(groupbox_form_layout, 1, 0, 1, 1)

        groupbox_2 = QGroupBox('Form layout')
        form_layout_2 = QFormLayout(groupbox_2)

        label_line4 = QLabel('Line 1:')
        label_line4.setStyleSheet('font-size: 11pt;')
        text_edit_4 = QTextEdit()
        text_edit_4.setMaximumHeight(20)
        form_layout_2.addRow(label_line4, text_edit_4)

        label_line5 = QLabel('Line 2: ')
        label_line5.setStyleSheet('font-size: 11pt;')
        combo_box_below = QComboBox()
        combo_box_below.addItems([''])
        form_layout_2.addRow(label_line5, combo_box_below)

        label_line6 = QLabel('Line 3: ')
        label_line6.setStyleSheet('font-size: 11pt;')
        text_edit_6 = QSpinBox()
        text_edit_6.setMaximumHeight(20)
        form_layout_2.addRow(label_line6, text_edit_6)

        gridLayout.addWidget(groupbox_2, 2, 0, 1, 3)

        groupbox_paragraph = QGroupBox('')
        vbox_paragraph = QVBoxLayout(groupbox_paragraph)
        big_text_edit = QTextEdit()
        vbox_paragraph.addWidget(big_text_edit)

        gridLayout.addWidget(big_text_edit, 1, 1, 1, 2)
        text_box = QTextEdit()
        gridLayout.addWidget(text_box, 3, 0, 1, 3)  


        dialogBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        gridLayout.addWidget(dialogBox, 4, 0, 1, 3)  

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        central_widget = QWidget()
        central_widget.setLayout(gridLayout)
        self.setCentralWidget(central_widget)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Basic Layouts')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec_())

