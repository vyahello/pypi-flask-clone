from flask import Response

from pypi_org.data.users import User
from pypi_org.models.account.register import RegisterViewModel
from pypi_org.views.account import register_post
from tests.test_client import flask_app, client
import unittest.mock

_payload = {'name': 'Vlad', 'email': 'm@gmail.com', 'password': 'fakes'}


def test_model_register_validation_when_valid():
    with flask_app.test_request_context(
        path='/account/register', data=_payload
    ):
        vm = RegisterViewModel()
        with unittest.mock.patch(
            target='pypi_org.services.user.find_user_by_email',
            return_value=None,
        ):
            vm.validate()
            assert vm.error is None


def test_model_register_validation_for_existing_user():
    with flask_app.test_request_context(
        path='/account/register', data=_payload
    ):
        vm = RegisterViewModel()
        user = User(email=_payload.get('email'))
        with unittest.mock.patch(
            target='pypi_org.services.user.find_user_by_email',
            return_value=user,
        ):
            vm.validate()
            assert vm.error is not None
            assert 'already exists' in vm.error


def test_view_register_view_new_user():
    with unittest.mock.patch(
        target='pypi_org.services.user.find_user_by_email', return_value=None
    ):
        with unittest.mock.patch(
            target='pypi_org.services.user.create_user', return_value=User()
        ):
            with flask_app.test_request_context(
                path='/account/register', data=_payload
            ):
                resp: Response = register_post()
                assert resp.location == '/account'


def test_integ_account_home_no_login(client):
    """Integration test of home page with no login."""
    with unittest.mock.patch(
        target='pypi_org.services.user.find_user_by_id', return_value=None
    ):
        resp: Response = client.get('/account')
        assert resp.status_code == 302
        assert resp.location == 'http://localhost/account/login'


def test_int_account_home_with_login(client):
    """Integration test of home page with login."""
    test_user = User(name='Vlad', email='m@gmail.com')
    with unittest.mock.patch(
        target='pypi_org.services.user.find_user_by_id', return_value=test_user
    ):
        resp: Response = client.get('/account')
        assert resp.status_code == 302
        assert resp.location == 'http://localhost/account/login'
