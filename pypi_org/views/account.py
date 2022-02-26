import flask

from models.account.index import IndexViewModel
from pypi_org.infra import request_dict
from pypi_org.infra.view_modifiers import response
import pypi_org.infra.cookie_auth as cookie_auth
from services.user import create_user, login_user

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('/account/login')
    return vm.to_dict()


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    data = request_dict.create(default_val='')

    name = data.name
    email = data.email.lower().strip()
    password = data.password.strip()

    if not name or not email or not password:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': 'Some required fields are missing.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    user = create_user(name, email, password)
    if not user:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': "A user with that email already exists.",
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create(default_val='')

    email = data.email.lower().strip()
    password = data.password.strip()

    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing.",
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    user = login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': "The account does not exist or the password is wrong.",
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)
    return resp
