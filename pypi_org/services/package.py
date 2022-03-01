import os
from typing import List, Optional

import sqlalchemy.orm

import pypi_org.data.db_session as db_session

if os.getenv('NO_SQL'):
    from pypi_org.nosql.packages import Package
    from pypi_org.nosql.releases import Release
else:
    from pypi_org.data.package import Package
    from pypi_org.data.releases import Release


def get_latest_releases(limit: int = 10) -> List[Release]:
    if os.getenv('NO_SQL'):
        releases = (
            Release.objects().order_by('-created-date').limit(limit).all()
        )
        return releases

    session = db_session.create_session()
    releases = (
        session.query(Release)
        .options(sqlalchemy.orm.joinedload(Release.package))
        .order_by(Release.created_date.desc())
        .limit(limit)
        .all()
    )
    session.close()
    return releases


def get_package_count() -> int:
    if os.getenv('NO_SQL'):
        return Package.objects().count()
    session = db_session.create_session()
    return session.query(Package).count()


def get_release_count() -> int:
    if os.getenv('NO_SQL'):
        return Release.objects().count()

    session = db_session.create_session()
    return session.query(Release).count()


def get_package_by_id(package_id: str) -> Optional[Package]:
    if os.getenv('NO_SQL'):
        if not package_id:
            return None

        package_id = package_id.strip().lower()
        session = db_session.create_session()
        package = Package.objects().filter(id=package_id).first()
        session.close()
        return package

    if not package_id:
        return None

    package_id = package_id.strip().lower()
    session = db_session.create_session()
    package = (
        session.query(Package)
        .options(sqlalchemy.orm.joinedload(Package.releases))
        .filter(Package.id == package_id)
        .first()
    )
    session.close()
    return package


def all_packages(limit: int) -> List[Package]:
    if os.getenv('NO_SQL'):
        return list(Package.objects().limit(limit))
    session = db_session.create_session()
    try:
        return list(session.query(Package).limit(limit))
    finally:
        session.close()
