# Создать файл sqlalchemy_13.py. Создать 5 книг. Получить всех студентов и добавить каждому студенту эти пять книг.
from school.models import session, Book, Student

arr = [
    Book('one', 35),
    Book(name='two', pages=500),
    Book('-3', 70),
    Book('Math', 120),
    Book('English', 300)
]

session.add_all(arr)
session.commit()
students_all = session.query(Student).all()
books_all = session.query(Book).all()

for book in books_all:
    book.students = students_all

session.commit()

