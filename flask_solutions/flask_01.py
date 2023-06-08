from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/g/')
def time_now():
    return f"{datetime.now()}"


@app.route('/g/g/')
def time_now_new():
    return f"modern view of date - {datetime.now()}"


if __name__ == '__main__':
    app.run()
