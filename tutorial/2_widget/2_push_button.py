import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PySide6.QtGui import QFont, QIcon, QAction
from PySide6.QtCore import QSize


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 500, 700, 700)
        self.create_button()

    def create_button(self):
        btn = QPushButton('Click', self)
        btn.setGeometry(100, 100, 200, 100)
        btn.setFont(QFont('Times', 14, QFont.ExtraBold))
        btn.setIcon(QIcon('../image/icon.jpg'))
        btn.setIconSize(QSize(36, 36))

        # PySide6 popup menu 目前有問題 PyQt6 正常執行 (20220605)
        # https://www.pythonfixing.com/2022/01/fixed-pyside-qpushbutton-right-click.html
        menu = QMenu()
        menu.addAction('action 1')
        menu.addAction('action 2')
        menu.addAction('action 3')
        btn.setMenu(menu)
        menu.show()
        

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
