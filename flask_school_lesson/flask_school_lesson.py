from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskschoollesson.db'
db = SQLAlchemy(app)


class BaseForSchool(db.Model):

    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Group(BaseForSchool):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Student(BaseForSchool):
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    group_id = db.Column(db.Integer, ForeignKey(Group.id), nullable=True)
    group = relationship('Group', foreign_keys='Student.group_id', backref='students')


@app.route('/')
def read_groups():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)


@app.route('/add_group/', methods=['POST', 'GET'])
def add_group():
    if request.method == 'GET':
        return render_template('form_add_group.html')
    else:
        group = Group(name=request.form['name'])
        group.save()
        return redirect(url_for('read_groups'))


@app.route('/students/<group_id>')
def students(group_id):
    students = Student.query.filter_by(group_id=group_id)
    return render_template('index_students.html', students=students, group_id=group_id)


@app.route('/add_student/', methods=['POST', 'GET'])
def add_student():
    if request.method == 'GET':
        group_id = request.args.get('group_id')
        return render_template('form_add_student.html', group_id=group_id)
    else:
        group_id = request.args.get('group_id')
        student = Student(firstname=request.form['firstname'], lastname=request.form['lastname'],
                          group_id=group_id)
        student.save()
        return redirect(url_for('students', group_id=group_id))


@app.route('/delete_student/')
def delete_student():
    student_id = request.args.get('student_id')
    student = db.session.query(Student).get(student_id)
    student.delete()
    return redirect(url_for('students', group_id=request.args.get('group_id')))


@app.route('/update_student/', methods=['POST', 'GET'])
def update_student():
    if request.method == 'GET':
        student_id = request.args.get('student_id')
        student = db.session.query(Student).get(student_id)
        return render_template('form_update_student.html', student=student)
    else:
        student_id = request.args.get('student_id')
        student = db.session.query(Student).get(student_id)
        setattr(student, 'firstname', request.form['firstname'])
        setattr(student, 'lastname', request.form['lastname'])
        setattr(student, 'group_id', request.form['group_id'])
        student.update()
        return redirect(url_for('students', group_id=request.form['group_id']))


@app.route('/update_group/', methods=['POST', 'GET'])
def update_group():
    if request.method == 'GET':
        group_id = request.args.get('group_id')
        return render_template('form_update_group.html', group_id=group_id)
    else:
        group = db.session.query(Group). \
            filter_by(id=request.args.get('group_id')). \
            first()
        # group = Group.query.get(request.args.get('group_id'))
        group.name = request.form['name']
        group.update()
        return redirect(url_for('read_groups'))


@app.route('/delete_group/')
def delete_group():
    group_id = request.args.get('group_id')
    # Group.query.delete(group_id)
    group = db.session.query(Group).get(group_id)
    group.delete()
    return redirect(url_for('read_groups'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
