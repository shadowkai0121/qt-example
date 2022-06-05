import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 700, 700)
        self.setupUi()
    
    def setupUi(self):
        hbox = QHBoxLayout()
        self.label = QLabel('Default')
        btn = QPushButton('Click Me')

        # btn 被點擊的時候會產生 signal 由 Window 的 clicked_btn 作為 Slot 接收
        btn.clicked.connect(self.clicked_btn)

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText('Clicked!!!!!')
        font = self.label.font()
        font.setPixelSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('color: red')


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
