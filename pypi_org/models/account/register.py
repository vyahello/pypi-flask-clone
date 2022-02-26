from models.shared.modelbase import ViewModelBase
from services.user import find_user_by_id


class RegisterViewModel(ViewModelBase):
    def __init__(self) -> None:
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()
        self.age = self.request_dict.age.strip()

    def validate(self) -> None:
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name'
        elif not self.email or not self.email.strip():
            self.error = 'You must specify an email'
        elif not self.password or not self.password.strip():
            self.error = 'You must specify a password'
        elif len(self.password.strip()) < 5:
            self.error = 'Password must be at least 5 characters'
        elif find_user_by_id(self.email):
            self.error = 'User with that email address already exists'
