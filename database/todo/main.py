import sys
from PySide6 import QtWidgets
from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 註冊 ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # signal & slot
        self.ui.create_button.released.connect(self.create_todo)
        self.ui.done_button.released.connect(self.done_todo)
        self.ui.delete_button.released.connect(self.delete_todo)

    def delete_todo(self):
        # 測試按鈕功能
        self.ui.create_todo_text_edit.setText('delete todo')

    def done_todo(self):
        # 測試按鈕功能
        self.ui.create_todo_text_edit.setText('done todo')

    def create_todo(self):
        # 取得輸入框資料
        todo = self.ui.create_todo_text_edit.text()
        self.ui.todo_list.addItem(todo)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
