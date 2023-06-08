# Создать сайт. При запросе по урлу /my_word/[word],
# в случае если длина слова четна - выводить строку содержащую все
# нечетные элементы строки(abcdef -> ace). В ином случае перенаправлять на домашнюю страницу.
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/my_word/<world>')
def my_word(world):
    if len(world) % 2:
        return redirect(url_for('hello'))
    else:
        result = world[::2]
        return result


if __name__ == '__main__':
    app.run()
