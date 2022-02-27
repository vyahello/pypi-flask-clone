from pypi_org.models.shared.modelbase import ViewModelBase
from pypi_org.services.user import find_user_by_id


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = find_user_by_id(self.user_id)
