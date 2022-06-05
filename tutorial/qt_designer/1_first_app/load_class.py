import sys
from PySide6.QtWidgets import QApplication, QWidget
from first_app import Ui_Form


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
