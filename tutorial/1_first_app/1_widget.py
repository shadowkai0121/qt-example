import sys
from PySide6.QtWidgets import QApplication, QWidget

# QApplication class 控制整個 GUI 的流程與設定
# QApplication 特化了 QGUI 一些基於 QWidget 所需的功能
app = QApplication(sys.argv) # 使用 command line 參數
# app = QApplication()


# 建立 QApplication 之後需要建立視窗物件(QWidget, QMainWindow, QDialog)
'''
QWidget:
是所有 UI 物件的基礎
'''
window = QWidget()
window.show()

# app.exec() 會啟動 Event loop 並且在意外終止後呼叫 sys.exit 進行退出
sys.exit(app.exec())