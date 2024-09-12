import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDockWidget, QStatusBar, QToolBar, QTextEdit, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import Qt, QTimer

class ComponenteBase:
    def __init__(self, barra_estado):
        self.barra_estado = barra_estado
        self.barra_estado.showMessage("Listo. Esperando acción", 3000)

        sistema_operativo = "Linux" if sys.platform.startswith("linux") else "Windows"
        etiqueta_sistema = QLabel(sistema_operativo)
        etiqueta_sistema.setAlignment(Qt.AlignRight)
        self.barra_estado.addPermanentWidget(etiqueta_sistema)

        temporizador = QTimer()
        temporizador.timeout.connect(self.cambiar_texto_automatico)
        temporizador.start(3001)

    def cambiar_texto_automatico(self):
        self.barra_estado.showMessage("Imprimir por consola")

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.barra_estado = QStatusBar()  # Utiliza una única instancia de QStatusBar
        self.setStatusBar(self.barra_estado)

        self.construir_docks()
        self.construir_etiqueta_principal()

        self.setWindowTitle("Aplicación")
        self.setGeometry(100, 100, 600, 400)

        barra_menu = self.menuBar()
        menu_principal = barra_menu.addMenu("Menú")

        accion_menu_principal = QAction("Imprimir por consola", self)
        accion_menu_principal.setShortcut("Ctrl+P")
        accion_menu_principal.setIcon(QIcon("Activitat3/animal-dog.png"))
        accion_menu_principal.triggered.connect(self.accion_imprimir)
        menu_principal.addAction(accion_menu_principal)

        barra_herramientas = QToolBar("Barra de Herramientas")
        barra_herramientas.addAction(accion_menu_principal)
        self.addToolBar(barra_herramientas)

        self.barra_estado.setToolTip("Imprimir por consola")

    def accion_imprimir(self):
        print("Acción lanzada a través del menú, del atajo o de la barra de herramientas")

    def construir_docks(self):
        dock = QDockWidget()
        dock.setWindowTitle("Componente base 1")
        text_edit = QTextEdit()
        dock.setWidget(text_edit)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        dock.setMinimumWidth(125)
        dock.setMinimumHeight(100)
        dock.setMinimumSize(125, 100)

    def construir_etiqueta_principal(self):
        layout = QVBoxLayout()
        etiqueta = QLabel("Componente principal")
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        etiqueta.setMinimumWidth(125)
        etiqueta.setMinimumHeight(100)
        etiqueta.setMinimumSize(125, 100)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    componente_base = ComponenteBase(ventana.barra_estado)
    ventana.show()
    app.exec_()
