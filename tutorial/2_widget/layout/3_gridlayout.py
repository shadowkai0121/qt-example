import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 700, 700)

        grid = QGridLayout()

        btn1 = QPushButton('One')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')
        btn4 = QPushButton('Four')
        btn5 = QPushButton('Five')

        grid.addWidget(btn1, 1, 0)
        grid.addWidget(btn2, 1, 0) # 同一格會後蓋前
        grid.addWidget(btn3, 1, 4) # 空 column 會被忽略
        grid.addWidget(btn4, 2, 1)
        grid.addWidget(btn5, 3, 1)
        


        self.setLayout(grid)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
