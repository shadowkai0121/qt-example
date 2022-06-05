import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 700, 700)
        vbox = QVBoxLayout()

        btn1 = QPushButton('One')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addStretch()
        vbox.addWidget(btn3)
        # vbox.addSpacing(50)

        self.setLayout(vbox)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
