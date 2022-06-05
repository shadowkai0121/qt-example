import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # x, y, width, height
        self.setGeometry(0, 0, 700, 400)
        self.setWindowTitle('這裡是title')
        self.setWindowIcon(QIcon('../image/icon.jpg'))

        # 設定了之後無法使用視窗最大化
        # self.setFixedHeight(700)
        # self.setFixedWidth(400)

        self.setStyleSheet('background-color: green')
        self.setWindowOpacity(0.5)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
