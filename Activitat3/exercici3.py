from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QAction,QIcon

class ImageWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        label = QLabel(self)
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setWindowTitle("Exemple menú")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(280, 120)
        self.image_window_2 = None
        self.image_window_3 = None
        self.construir_menu()
        self.setWindowTitle("Exemple de menú")

    def construir_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&File")
        action_bot_1 = QAction("&Botó 1", self)
        action_bot_1.setIcon(QIcon("Activitat3/animal-dog.png"))
        menu_archivo.addAction(action_bot_1)

        submenu_archivo = menu_archivo.addMenu("&Submenú")

        action_2 = QAction("Botó 2", self)
        action_2.setIcon(QIcon("Activitat3/animal-dog.png")) 
        action_2.triggered.connect(self.abrir_ventana_imagen_2)
        submenu_archivo.addAction(action_2)

        action_3 = QAction("Botó 3", self)
        action_3.setIcon(QIcon("Activitat3/animal-monkey.png")) 
        action_3.triggered.connect(self.abrir_ventana_imagen_3)
        submenu_archivo.addAction(action_3)

    def abrir_ventana_imagen_2(self):
        if not self.image_window_2:
            self.image_window_2 = ImageWindow("Activitat3/perro.jpeg")
        self.image_window_2.show()

    def abrir_ventana_imagen_3(self):
        if not self.image_window_3:
            self.image_window_3 = ImageWindow("Activitat3/mono.jpeg")
        self.image_window_3.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

