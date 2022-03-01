import os
from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import pypi_org.data.db_session as db_session

if os.getenv('NO_SQL'):
    from pypi_org.nosql.users import User
else:
    from pypi_org.data.users import User


def get_user_count() -> int:
    if os.getenv('NO_SQL'):
        return User.objects().count()
    else:
        session = db_session.create_session()
        return session.query(User).count()


def find_user_by_email(email: str) -> Optional[User]:
    if os.getenv('NO_SQL'):
        return User.objects().filter(email=email).first()
    else:
        session = db_session.create_session()
        return session.query(User).filter(User.email == email).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None
    if os.getenv('NO_SQL'):
        user = User()
        user.email = email
        user.name = name
        user.hashed_password = hash_text(password)
        user.save()
    else:
        user = User()
        user.email = email
        user.name = name
        user.hashed_password = hash_text(password)
        session = db_session.create_session()
        session.add(user)
        session.commit()
    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    if os.getenv('NO_SQL'):
        user = find_user_by_email(email)
    else:
        session = db_session.create_session()
        user = session.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None
    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    if os.getenv('NO_SQL'):
        user = User.objects().filter(id=user_id).first()
    else:
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
    return user
