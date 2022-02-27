import flask

from pypi_org.services import package
from pypi_org.models.shared.modelbase import ViewModelBase


class SiteMapViewModel(ViewModelBase):
    def __init__(self, limit: int):
        super().__init__()
        self.packages = package.all_packages(limit)
        self.last_updated_text = "2022-02-22"
        self.site = "{}://{}".format(flask.request.scheme, flask.request.host)
