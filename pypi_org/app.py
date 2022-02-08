import flask

from infra.view_modifiers import response

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'passlib', 'version': '2.4.0'},
    ]


@app.route('/')
@response(template_file='home/index.html')
def index():
    return {'packages': get_latest_packages()}


@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
