from pypi_org.models.account.register import RegisterViewModel
from tests.test_client import flask_app
import unittest.mock


def test_register_validation_when_valid():
    form_data = {'name': 'Vlad', 'email': 'm@gmail.com', 'password': 'fakes'}
    with flask_app.test_request_context(
        path='/account/register', data=form_data
    ):
        vm = RegisterViewModel()

    target = 'pypi_org.services.user.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    assert vm.error is None
