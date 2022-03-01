import ssl

import mongoengine


def global_init(
    user=None,
    password=None,
    port=27017,
    server='localhost',
    use_ssl=True,
    db_name: str = 'pypi',
):
    if user or password:
        data = {
            'username': user,
            'password': password,
            'port': port,
            'host': server,
            'authentication_source': 'admin',
            'authentication_mechanism': 'SCRAM-SHA-1',
            'ssl': use_ssl,
            'ssl_cert_reqs': ssl.CERT_NONE,
        }
        mongoengine.register_connection(alias='core', name=db_name, **data)
        data['password'] = '*' * 13
        print('[MongoDB] Registering prod connection: {}'.format(data))
    else:
        print('[MongoDB] Registering dev connection')
        mongoengine.register_connection(alias='core', name=db_name)
