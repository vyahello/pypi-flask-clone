import flask

from pypi_org.views import cms, home, package

app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    app.register_blueprint(home.blueprint)
    app.register_blueprint(package.blueprint)
    app.register_blueprint(cms.blueprint)


if __name__ == '__main__':
    main()
