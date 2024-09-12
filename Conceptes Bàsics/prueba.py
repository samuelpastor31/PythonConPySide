from PySide6.QtWidgets import QApplication, QWidget
import sys
# Creamos una aplicación para gestionar la interfaz
app = QApplication(sys.argv)
# Creamos un widget para generar la ventana
window = QWidget()
# Mostramos la ventana, se encuentra oculta por defecto
window.show()
# Iniciamos el bucle del programa
sys.exit(app.exec_())