import flask

from pypi_org.infra import cookie_auth, request_dict


class ViewModelBase:
    def __init__(self):
        self.request = flask.request
        self.request_dict = request_dict.create('')
        self.error = None
        self.user_iod = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self) -> dict:
        return self.__dict__
