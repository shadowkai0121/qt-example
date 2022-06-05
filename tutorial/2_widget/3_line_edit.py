import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 500, 700, 700)

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Sanserif', 14))

        # 預設值
        # line_edit.setText('Default')

        line_edit.setPlaceholderText('Please input....')

        # line_edit.setEnabled(False)

        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
