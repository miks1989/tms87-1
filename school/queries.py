from school.models import Group, session, Student

students_all = session.query(Student).all()
groups = session.query(Group).all()
print(students_all)
for student in students_all:
    print(student.firstname, student)

for group in groups:
    students_of_one_group = group.students
    print(students_of_one_group)
    print([st.firstname for st in students_of_one_group])
    for st in group:
        print(st)


session.commit()
