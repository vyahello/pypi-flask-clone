import flask

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'passlib', 'version': '2.4.0'},
    ]


@app.route('/')
def index():
    return flask.render_template('index.html', packages=get_latest_packages())


@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
