import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run()
