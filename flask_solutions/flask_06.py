import csv
import os.path

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/all/')
def all_users():
    with open('flask_users_05.csv', 'r') as file:
        csvreader = csv.reader(file)
        #test comment
        rows = [row for row in csvreader]
    return render_template('all.html', users=rows[1:])






@app.route('/', methods=['POST', 'GET'], endpoint='custom_login')
def login():
    if request.method == 'POST':
        user = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        data = request.form
        with open('flask_users_05.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([user, lastname, age])

        result = render_template('form_6_added.html', data_for_template=data)
        return result
    else:
        return render_template('form_6.html')


if __name__ == '__main__':
    if not os.path.exists('flask_users_05.csv'):
        with open('flask_users_05.csv', 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["user", 'lastname', 'age'])
    app.run()
