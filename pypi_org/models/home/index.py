from pypi_org.services import user, package
from pypi_org.models.shared.modelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.releases = package.get_latest_releases()
        self.package_count = package.get_package_count()
        self.release_count = package.get_release_count()
        self.user_count = user.get_user_count()
