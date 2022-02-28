import os

import flask

from pypi_org.views import cms, home, package, account, seo

from pypi_org.data.db_session import global_init

app = flask.Flask(__name__)


def main():
    configure()
    app.run(debug=True)


def configure():
    print('Configuring Flask app:')

    register_blueprints()
    print('Registered blueprints')

    setup_db()
    print('DB setup completed.')
    print('', flush=True)


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'pypi.sqlite')
    global_init(db_file)


def register_blueprints():
    app.register_blueprint(home.blueprint)
    app.register_blueprint(package.blueprint)
    app.register_blueprint(cms.blueprint)
    app.register_blueprint(account.blueprint)
    app.register_blueprint(seo.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()
