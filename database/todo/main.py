import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QDir
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect_database()

        # 註冊 ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_todo_list()

        # signal & slot
        self.ui.create_button.released.connect(self.create_todo)
        self.ui.done_button.released.connect(self.done_todo)
        self.ui.delete_button.released.connect(self.delete_todo)
    
    def set_todo_list(self):
        self.ui.todo_list.clear()
        self.todo_list = QSqlQueryModel()
        self.todo_list.setQuery('SELECT * FROM todo_list')
        for i in range(self.todo_list.rowCount()):
            id = self.todo_list.record(i).value('id')
            todo = self.todo_list.record(i).value('todo')
            is_done = bool(self.todo_list.record(i).value('is_done'))
            list_item = QtWidgets.QListWidgetItem(f'[{id}] {todo} ({is_done})')
            self.ui.todo_list.addItem(list_item)


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

    def connect_database(self):
        connection = QSqlDatabase.addDatabase('QSQLITE')
        connection.setDatabaseName('example.db')
        connection.open()
        self.db = connection


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
