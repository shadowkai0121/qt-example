import sys
from PySide6.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 700, 700)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
