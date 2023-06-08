from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def two_pow():
    return f'hello'


@app.route('/hello/<name>/<int:count>')
def hello_with_name(name, count):
    return f'hello, {name}, вы запросили {count} грамм воды'


@app.route('/hello_admin/')
def hello_admin():
    return f'hello admin'


@app.route('/hello_user/<name>')
def hello_user(name):
    print(f'{name} from hello_url')
    return f'{name} from hello_url'


@app.route('/hello/<name>/')
def hello_name(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', name=name))


if __name__ == '__main__':
    app.run()
