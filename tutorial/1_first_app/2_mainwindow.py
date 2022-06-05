import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

'''
Main window 提供建立 UI 所需的框架
他有自己的 Layout 以及相關的物件 ex: QToolBars, QDockWidgets, QMenuBar, QStatusBar
'''
window = QMainWindow()
window.statusBar().showMessage('Welcome to PySide6')
window.menuBar().addMenu('Here is Menu Bar')
window.show()

sys.exit(app.exec())