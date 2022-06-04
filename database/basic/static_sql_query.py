import sys
from PySide6.QtSql import QSqlQuery

# 建立連線
from create_connection import connection

# 檢查連線
if not connection.isOpen():
    print(f'Database Error: {connection.lastError().databaseText()}')
    sys.exit(1)

# SQL 語法
create_table_sql = '''
CREATE TABLE todo_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    todo VARCHAR(50) NOT NULL,
    is_done TINYINT(1)
)
'''

# 使用 QSqlQuery 物件
query = QSqlQuery()
result = query.exec(create_table_sql)

# table 重複的狀況會回傳 False
print(f'create table result: {result}')
if not result:
    print(f'Database Error: {query.lastError().databaseText()}')
    # Database Error: table todo_list already exists
    sys.exit(1)

