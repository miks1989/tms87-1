from models import session, Group, Student, Diary

# data = session.query(Group, Student).join(Group, Group.id == Student.group_id).all()
# print(data)
# for gr, st in data:
#     print(st.firstname, gr.name)



result2 = session.query(Student, Diary).join(Diary, Student.id == Diary.student_id).filter(Diary.avg_score > 5)
print(list(result2))
for st, d in result2:
    print(st.firstname, d.avg_score)
