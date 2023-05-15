import sqlite3 as sq

connection = sq.connect('test.db')
cur = connection.cursor()
print(cur.execute('select * from book'))
data = cur.execute('select * from book')
for book in data:
    print(book)
connection.close()
