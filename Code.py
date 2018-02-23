from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'We gon\' take you to school'


if __name__ == '__main__':
    app.run()
