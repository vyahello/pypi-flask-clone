from flask import Response

from tests.test_client import flask_app, client
from pypi_org.views import home


def test_integ_homepage(client):
    resp: Response = client.get('/')
    assert resp.status_code == 200
    assert b'Find, install and publish Python packages' in resp.data


def test_view_homepage_directly():
    with flask_app.test_request_context(path='/'):
        resp: Response = home.index()
        assert resp.status_code == 200
        assert len(resp.model.get('releases')) > 0
