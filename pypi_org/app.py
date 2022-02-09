import flask

from pypi_org.views import home, package

app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    app.register_blueprint(home.blueprint)
    app.register_blueprint(package.blueprint)


if __name__ == '__main__':
    main()
