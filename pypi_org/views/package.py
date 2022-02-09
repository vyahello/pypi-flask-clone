import flask

from infra.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='home/index.html')
def package_details(package_name: str) -> dict:
    return {'packages': ['Package details for {}'.format(package_name)]}
