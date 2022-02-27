from pypi_org.data.users import User
from pypi_org.models.account.register import RegisterViewModel
from tests.test_client import flask_app
import unittest.mock

_payload = {'name': 'Vlad', 'email': 'm@gmail.com', 'password': 'fakes'}


def test_register_validation_when_valid():
    with flask_app.test_request_context(
        path='/account/register', data=_payload
    ):
        vm = RegisterViewModel()
        target = 'pypi_org.services.user.find_user_by_email'
        with unittest.mock.patch(target, return_value=None):
            vm.validate()
            assert vm.error is None


def test_register_validation_for_existing_user():
    with flask_app.test_request_context(
        path='/account/register', data=_payload
    ):
        vm = RegisterViewModel()
        target = 'pypi_org.services.user.find_user_by_email'
        user = User(email=_payload.get('email'))
        with unittest.mock.patch(target, return_value=user):
            vm.validate()
            assert vm.error is not None
            assert 'already exists' in vm.error
