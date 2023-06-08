from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/<name>/<lastname>')
def success(name, lastname):
    return f'hello {name} {lastname}'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form, type(request.form))
        user = request.form['name']
        lastname = request.form['lastname']
        return redirect(url_for('success', name=user, lastname=lastname))
    # else:
    #     user = request.args.get('name')
    #     return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
