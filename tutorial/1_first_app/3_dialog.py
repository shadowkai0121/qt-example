import sys
from PySide6.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)

'''
對話框的基礎類別，對話框通常是 short-term tasks 用來與 User 簡短的交流
QDialog 沒辦法最小化或最大化
May be modal(彈出新視窗) or modeless(視窗內例如 ctrl + f 搜尋框)
'''
window = QDialog()
window.show()

sys.exit(app.exec())