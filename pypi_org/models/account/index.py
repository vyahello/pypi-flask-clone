from models.shared.modelbase import ViewModelBase
from services.user import find_user_by_id


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = find_user_by_id(self.user_id)
