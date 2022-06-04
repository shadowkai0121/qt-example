from operator import mod
import sys
from PySide6.QtSql import QSqlQueryModel, QSqlTableModel

# 建立連線
from create_connection import connection

# 檢查連線
if not connection.isOpen():
    print(f'Database Error: {connection.lastError().databaseText()}')
    sys.exit(1)

model = QSqlQueryModel()
model.setQuery('SELECT * FROM todo_list')
for i in range(model.rowCount()):
    id = model.record(i).value('id')
    todo = model.record(i).value('todo')
    is_done = model.record(i).value('is_done')
    print(f'row[{i}]=(id = {id}, todo = {todo}, is_done = {is_done})')


# QSqlTableModel 是 QSqlQueryModel 的子類別
# 可以直接跟 TableView 一起操作
model = QSqlTableModel()
model.setTable('todo_list')
model.select()
for i in range(model.rowCount()):
    id = model.record(i).value('id')
    todo = model.record(i).value('todo')
    is_done = model.record(i).value('is_done')
    print(f'row[{i}]=(id = {id}, todo = {todo}, is_done = {is_done})')


