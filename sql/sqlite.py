import sqlite3 as sq

connection = sq.connect('test.db')
cur = connection.cursor()
print(cur.execute('select * from user'))
data = cur.execute('select * from user')
for book in data:
    print(book)
connection.close()
