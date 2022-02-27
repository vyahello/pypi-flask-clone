import datetime
import unittest.mock
from tests.test_client import flask_app, client
from pypi_org.views.package import package_details
from pypi_org.data.package import Package
from pypi_org.data.releases import Release

from flask import Response


def test_package_details_success():
    # Arrange
    test_package = Package()
    test_package.id = 'sqlalchemy'
    test_package.description = 'TDB'
    test_package.releases = [
        Release(
            created_date=datetime.datetime.now(),
            major_ver=1,
            minor_ver=2,
            build_ver=200,
        ),
        Release(
            created_date=datetime.datetime.now() - datetime.timedelta(days=10)
        ),
    ]

    with unittest.mock.patch(
        'pypi_org.services.package.get_package_by_id',
        return_value=test_package,
    ):
        with flask_app.test_request_context(path='/project/' + test_package.id):
            resp: Response = package_details(test_package.id)

    assert b'sqlalchemy 1.2.200' in resp.data


def test_package_details_404(client):
    """Integration test of package details."""
    with unittest.mock.patch(
        target='pypi_org.services.package.get_package_by_id', return_value=None
    ):
        resp: Response = client.get('sqlalchemy_missing')
        assert resp.status_code == 404
