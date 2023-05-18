import sqlite3 as sq

# with sq.connect('test.db') as connection:

connection = sq.connect('test.db')
# cur = connection.cursor()
# connection.execute("""CREATE TABLE user (
#    id integer primary key autoincrement,
#    firstname varchar(255),
#    lastname varchar(255),
#    age integer
# );""")

# connection.execute("""INSERT INTO user(firstname, lastname, age)
#  values ('max', 'ivanov', 25),
# ('max', 'petrov', 17),
# ('vasya', 'petrov', 16),
# ('pyatro', 'petrovich', 20),
# ('max', 'makar', 23);""")
#
# connection.commit()

data = connection.execute("SELECT * FROM user WHERE firstname='max';")
for i in data:
    print(i)
#
#
print("WHERE age<25")
data = connection.execute("SELECT * FROM user WHERE age<25;")
for i in data:
    print(i)

connection.close()
