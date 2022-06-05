import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 500, 700, 700)
        hbox = QHBoxLayout()

        btn1 = QPushButton('One')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')

        hbox.addWidget(btn1)

        # 增加間隔
        hbox.addSpacing(100)

        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        self.setLayout(hbox)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
