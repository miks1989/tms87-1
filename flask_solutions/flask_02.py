from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def two_pow(number):
    return f"2 ** {number} = {2 ** number}"


if __name__ == '__main__':
    app.run()
