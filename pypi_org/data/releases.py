import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id: int = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )

    major_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    minor_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    build_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    created_date: datetime.datetime = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now, index=True
    )
    comment: str = sqlalchemy.Column(sqlalchemy.String)
    url: str = sqlalchemy.Column(sqlalchemy.String)
    size: int = sqlalchemy.Column(sqlalchemy.BigInteger)

    # Package relationship

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
