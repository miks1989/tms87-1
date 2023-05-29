from models import session, Group, Student, Diary

data = session.query(Group).join(Student, Group.id == Student.group_id).filter(Student.firstname == 'max').all()
print(data)
for i in data:
    print(i.name)



result2 = session.query(Student, Diary).join(Diary, Student.id == Diary.student_id).filter(Diary.avg_score > 5)
print(list(result2))
for st, d in result2:
    print(st.firstname, d.avg_score)
