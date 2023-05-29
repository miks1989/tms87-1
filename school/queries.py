from school.models import Group, session, Student, Book

# students_all = session.query(Student).all()
groups = session.query(Group).all()
# print(students_all)
# for student in students_all:
#     print(student.firstname, student)
#
for group in groups:
    students_of_one_group = group.students
    print(students_of_one_group)
    print([st.books for st in students_of_one_group])
#
# books = session.query(Book).all()
#
# for book in books:
#     students_for_book = book.students
#     print([st.firstname for st in students_for_book])

session.commit()
