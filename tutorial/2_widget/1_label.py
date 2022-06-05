import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QPixmap, QMovie


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 500, 700, 700)
        # self.basic()
        # self.use_pixmap()
        self.use_gif()

    def basic(self):
        # 建構時綁定文字與上層
        label = QLabel('PySide6', self)

        # 設置樣式
        label.setStyleSheet('color: red')

        # 動態設置文字
        label.setText('Yo')

        # 移動相對位置
        label.move(200,200)
        
        # 直接產生新的字型套用
        font = QFont('Sanserif', 10)
        label.setFont(font)

        # 取得現有的字型進行設定
        font = label.font()
        font.setPointSize(50)
        font.setBold(True)
        label.setFont(font)

        # 清空內容
        label.clear()

    def use_pixmap(self):
        label = QLabel(self)
        pixmap = QPixmap('../image/icon.jpg')
        label.setPixmap(pixmap)

    def use_gif(self):
        label = QLabel(self)
        # QMove 用來顯示簡單的無聲動畫 ex: gif
        movie = QMovie('../image/who_am_i.gif')
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
