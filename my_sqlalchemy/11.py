# Создать таблицу Студент(Student) с помощью sqlalchemy в файле models.py.
# Студент характеризуется именем(firstname) и фамилией(lastname)
# и группой к которой он приурочен.
#
# Создать файл sqlalchemy_11.py. Создать две группы. Добавить
# в каждую по три студента.
from school.models import Group, Student, session

group_1 = Group('fm1')
group_2 = Group('fm2')

student_1 = Student('max', 'ivanov', group=group_1)
student_2 = Student('igar', 'ivanovich', group=group_1)
student_3 = Student('Valera', 'ivanko', group=group_1)
student_4 = Student('far', 'petrov', group=group_2)
student_5 = Student('har', 'petrovich', group=group_2)
student_6 = Student('baks', 'gari', group=group_2)

session.add_all([group_1, group_2, student_1,
                 student_2, student_3, student_4,
                 student_5, student_6])
session.commit()

# Описать модель школьного дневника(Diary) с помощью
# sqlalchemy в файле models.py. Дневник характеризуется
# Средним баллом и студентом к которому он приурочен.
#
# Создать файл sqlalchemy_12.py.
# Получить всех студентов и создать для каждого дневник.


from school.models import session, Student, Diary

students_all = session.query(Student).all()
arr = [Diary(5.5, students_all[0]),
       Diary(5.8, students_all[1]),
       Diary(6, students_all[2]),
       Diary(7, students_all[3]),
       Diary(8, students_all[4]),
       Diary(4, students_all[5])
       ]
session.add_all(arr)
session.commit()


# Описать модель Книга(Book) с помощью sqlalchemy в файле models.py.
# Книга характеризуется названием, количеством страниц и студентами
# у которых эта книга.
#
# Создать файл sqlalchemy_13.py. Создать 5 книг.
# Получить всех студентов и добавить каждому студенту эти пять книг.
from school.models import session, Book, Student

session.add_all([Book('one', 35),
                 Book(name='two', pages=500),
                 Book('-3', 70),
                 Book('Math', 120),
                 Book('English', 300)]
                )
session.commit()
students_all = session.query(Student).all()
books_all = session.query(Book).all()

for book in books_all:
    book.students = students_all

session.commit()



from school.models import session, Group, Student, Diary

result = session.query(Group, Student). \
    join(Student, Group.id == Student.group_id). \
    filter(Student.firstname == 'max')
for group, st in result:
    print(group.name, st.firstname)

print('-' * 15)

result2 = session.query(Student, Diary). \
    join(Diary, Student.id == Diary.student_id). \
    filter(Diary.avg_score > 6)
for st, d in result2:
    print(st.firstname, d.avg_score)
