from PySide6.QtSql import QSqlDatabase

# 建立連線
connection = QSqlDatabase.addDatabase('QSQLITE')
connection.setDatabaseName('example.db')
connection.open()

# 檢查連線
print(connection.isOpen())