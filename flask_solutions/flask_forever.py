# Создать сайт. При запросе по урлу /two_pow/[number]
# возвращает 2 в степени number
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def two_pow(number):
    assert isinstance(number, int)
    return f'2 ** {number} = {2 ** number}'


def time_now():
    return f'{datetime.now().date()}'

app.add_url_rule('/', 'time_now', time_now)

if __name__ == '__main__':
    app.run()