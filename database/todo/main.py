import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QDir
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
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

    def create_todo_list_item(self, id: int, todo:str , is_done: bool):
        list_item = QtWidgets.QListWidgetItem(todo)
        # 利用屬性儲存 id 而不顯示在畫面上
        list_item.id = id
        font = list_item.font()
        font.setStrikeOut(is_done)
        list_item.setFont(font)
        self.ui.todo_list.addItem(list_item)

    def set_todo_list(self):
        self.ui.todo_list.clear()
        self.todo_list = QSqlQueryModel()
        self.todo_list.setQuery('SELECT * FROM todo_list')
        for i in range(self.todo_list.rowCount()):
            id = self.todo_list.record(i).value('id')
            todo = self.todo_list.record(i).value('todo')
            is_done = bool(self.todo_list.record(i).value('is_done'))
            self.create_todo_list_item(id, todo, is_done)

    def delete_todo(self):
        item = self.ui.todo_list.currentItem()
        query = QSqlQuery()
        sql = '''
        DELETE FROM todo_list WHERE id = :id
        '''
        query.prepare(sql)
        query.bindValue(':id', item.id)
        result = query.exec()
        if result:
            row = self.ui.todo_list.currentRow()
            self.ui.todo_list.takeItem(row)

    def done_todo(self):
        # 測試按鈕功能
        self.ui.create_todo_text_edit.setText('done todo')

    def create_todo(self):
        # 取得輸入框資料
        todo = self.ui.create_todo_text_edit.text()

        query = QSqlQuery()
        sql = '''
        INSERT INTO todo_list(todo, is_done) VALUES (:todo, :is_done)
        '''
        query.prepare(sql)
        query.bindValue(':todo', todo)
        query.bindValue(':is_done', False)
        result = query.exec()
        if result:
            self.set_todo_list()

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
