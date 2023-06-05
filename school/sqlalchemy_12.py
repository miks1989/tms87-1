# Описать модель школьного дневника(Diary) с помощью
# sqlalchemy в файле models.py. Дневник характеризуется
# Средним баллом и студентом к которому он приурочен.
#
# Создать файл sqlalchemy_12.py.
# Получить всех студентов и создать для каждого дневник.


from school.models import session, Student, Diary

students_all = session.query(Student).all()

# arr = []
# for student in students_all:
#     avg_score = float(input(f'enter avg_score for student {student.firstname} - '))
#     diary = Diary(avg_score, student)
#     arr.append(diary)

arr = [Diary(avg_score=5.5, student=students_all[0]),
       Diary(avg_score=5.5, student=students_all[1]),
       Diary(avg_score=5.5, student=students_all[2]),
       Diary(avg_score=5.5, student=students_all[3]),
       Diary(avg_score=5.5, student=students_all[4]),
       Diary(avg_score=5.5, student=students_all[5])
       ]

# arr = [Diary(5.5, students_all[0]),
#        Diary(5.5, students_all[1]),
#        Diary(5.5, students_all[2]),
#        Diary(5.5, students_all[3]),
#        Diary(5.5, students_all[4]),
#        Diary(5.5, students_all[5])
#        ]

session.add_all(arr)
session.commit()
