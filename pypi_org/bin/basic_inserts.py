import os
import pypi_org.data.db_session as db_session
from data.package import Package


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    p = Package()
    p.id = input('Package ID')
    p.summary = input('Package Summary')
    p.author_name = input('Package Author')
    p.license = input('Package License')


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
