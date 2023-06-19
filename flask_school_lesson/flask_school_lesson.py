from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskschoollesson.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Student(db.Model):
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
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('read_groups'))


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
        db.session.commit()
        return redirect(url_for('read_groups'))


@app.route('/delete_group/')
def delete_group():
    group_id = request.args.get('group_id')
    # Group.query.delete(group_id)
    group = db.session.query(Group).filter_by(id=group_id)
    group.delete()
    db.session.commit()
    return redirect(url_for('read_groups'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
