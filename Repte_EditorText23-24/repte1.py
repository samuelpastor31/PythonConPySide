import sys
from PySide6.QtWidgets import QApplication, QFileDialog,QToolButton, QMainWindow, QStatusBar, QToolBar, QTextEdit
from PySide6.QtGui import QIcon,QAction
from PySide6.QtCore import Qt
from pathlib import Path


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)

        def absPath(file):
            return str(Path(__file__).parent.absolute() / file)

        self.setWindowTitle("Aplicación")
        self.setGeometry(100, 100, 600, 400)

        # Agrega un QTextEdit a la ventana principal
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(500,500,500,500)
        self.setCentralWidget(self.text_edit)

        # Configuración de la barra de herramientas
        barra_herramientas = QToolBar("Barra de Herramientas")
        self.addToolBar(barra_herramientas)

        # Botón Abrir
        button_abrir = QToolButton()
        button_abrir.setIcon(QIcon(absPath("images/open.png")))
        button_abrir.setText("Abrir archivo")
        button_abrir.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_abrir.clicked.connect(self.abrir_archivo)
        barra_herramientas.addWidget(button_abrir)

        # Botón Guardar
        button_guardar = QToolButton()
        button_guardar.setIcon(QIcon(absPath("images/guardar.png")))
        button_guardar.setText("Guardar a archivo")
        button_guardar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_guardar.clicked.connect(self.guardar_archivo)
        barra_herramientas.addWidget(button_guardar)

        # Configuración del menú
        barra_menu = self.menuBar()
        menu_principal = barra_menu.addMenu("Menú")

        # Acciones del menú
        open_action = QAction('Obrir arxiu', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.abrir_archivo)
        menu_principal.addAction(open_action)

        save_action = QAction('Guardar a arxiu', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.guardar_archivo)
        menu_principal.addAction(save_action)

        close_action = QAction('Tancar', self)
        close_action.setShortcut('Ctrl+W')
        close_action.triggered.connect(self.cerrar_archivo)
        menu_principal.addAction(close_action)

        exit_action = QAction('Eixir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        menu_principal.addAction(exit_action)

        self.archivo = None

    def abrir_archivo(self):
        ventana_dialogo = QFileDialog.getOpenFileName(
            self, caption="Abrir archivo ...", dir=".",
            filter="Documentos de texto (*.txt)",
            selectedFilter="Documentos de texto (*.txt)")
        self.archivo = ventana_dialogo[0]
        with open(self.archivo, "r+") as archivo:
            self.centralWidget().setText(archivo.read())

    def guardar_archivo(self):
        if self.archivo:
            with open(self.archivo, "w") as archivo:
                archivo.write(self.text_edit.toPlainText())
        else:
            self.guardar_como_archivo()

    def guardar_como_archivo(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            self, caption="Guardar a arxiu ...", dir=".", filter="Documentos de texto (*.txt)"
        )
        if file_path:
            self.archivo = file_path
            with open(self.archivo, "w") as archivo:
                archivo.write(self.text_edit.toPlainText())

    def cerrar_archivo(self):
        self.archivo = None
        self.text_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())