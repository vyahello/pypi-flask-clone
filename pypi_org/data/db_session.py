import sqlalchemy as sa
from sqlalchemy import orm

from data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory
    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception('You muse specify db file.')

    conn_str = f'sqlite:///{db_file.strip()}'
    engine = sa.create_engine(conn_str, echo=False)
    factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)
