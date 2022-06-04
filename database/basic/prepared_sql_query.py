import sys
from PySide6.QtSql import QSqlQuery

# 建立連線
from create_connection import connection

# 檢查連線
if not connection.isOpen():
    print(f'Database Error: {connection.lastError().databaseText()}')
    sys.exit(1)


#  .prepare() 產生 Prepared Statement
prepared_statement = QSqlQuery()

# # ODBC style
# prepared_statement.prepare(
#     """
#     INSERT INTO todo_list (
#         todo,
#         is_done
#     )
#     VALUES (?, ?)
#     """
# )

# # 綁定一筆資料
# prepared_statement.bindValue(0, 'ODBC style todo 1')

# # SQLite 參數型態不合一樣會寫入?!
# # prepared_statement.bindValue(1, '-- # ')
# prepared_statement.bindValue(1, False)

# result = prepared_statement.exec()
# print(f'ODBC style insert result: {result}')
# print(f'bound values: {prepared_statement.boundValues()}')

# Oracle style
prepared_statement.prepare(
    """
    INSERT INTO todo_list (
        todo,
        is_done
    )
    VALUES (:todo, :is_done)
    """
)

prepared_statement.bindValue(':todo', 'Oracle style todo 1')
prepared_statement.bindValue(':is_done', False)

result = prepared_statement.exec()
print(f'Oracle style insert result: {result}')
print(f'bound values: {prepared_statement.boundValues()}')

# 多筆新增
todo_list = [
    ('batch todo 1', True),
    ('batch todo 2', False),
    ('batch todo 3', False)
]

for todo, is_done in todo_list:
    prepared_statement.addBindValue(todo)
    prepared_statement.addBindValue(is_done)

    # 一樣是單筆執行
    result = prepared_statement.exec()
    print(f'Oracle style insert result: {result}')
    print(f'bound values: {prepared_statement.boundValues()}')


# 沒有資料表可以 insert 的狀況會回傳 False 但是沒有Error
if not result:
    print(f'Database Error: {prepared_statement.lastError().databaseText()}')
    sys.exit(1)

