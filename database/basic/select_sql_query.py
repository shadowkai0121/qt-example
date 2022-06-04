import sys
from PySide6.QtSql import QSqlQuery

# 建立連線
from create_connection import connection

# 檢查連線
if not connection.isOpen():
    print(f'Database Error: {connection.lastError().databaseText()}')
    sys.exit(1)

sql = '''
SELECT * FROM todo_list
'''
query = QSqlQuery()
result = query.exec(sql)

if not result:
    print(f'Database Error: {query.lastError().databaseText()}')
    sys.exit(1)

# 取得第一筆資料
result = query.first()
print(f'query response: {result}')
# DB 的 true false 實際上只有 0 1
# record: id = 1, todo = Oracle style todo 1, is_done = False
print(f'record: id = {query.value(0)}, todo = {query.value(1)}, is_done = {bool(query.value(2))}')

# next 會接續在上一次查詢之後的下一筆
result = query.next()
print(f'query response: {result}')
print(f'record: id = {query.value(0)}, todo = {query.value(1)}, is_done = {bool(query.value(2))}')
# record: id = 2, todo = batch todo 1, is_done = True

# 使用 finish 會釋放掉 query 的操作結果(first, next...etc)
query.finish()

# 直接執行前次的 sql 語法
query.exec()
result = query.next()
print(f'query response: {result}')
print(f'record: id = {query.value(0)}, todo = {query.value(1)}, is_done = {bool(query.value(2))}')
# record: id = 1, todo = Oracle style todo 1, is_done = False
