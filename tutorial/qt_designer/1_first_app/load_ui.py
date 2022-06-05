import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# todo: PySide6 Custom Widgets
# https://stackoverflow.com/questions/68528717/environment-variable-pyside-designer-plugins-is-not-set-bailing-out
class Window(QWidget):
    def __init__(self):
        super().__init__()
        ui_file = QFile('first_app.ui')
        ui_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(ui_file, self)
        ui_file.close()

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
