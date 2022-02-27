import flask

from pypi_org.infra.view_modifiers import response
from pypi_org.models.seo.sitemap import SiteMapViewModel

blueprint = flask.Blueprint('seo', __name__, template_folder='templates')


@blueprint.route('/sitemap.xml')
@response(mimetype='application/xml', template_file='seo/sitemap.html')
def sitemap():
    vm = SiteMapViewModel(1000)
    return vm.to_dict()


@blueprint.route('/robots.txt')
@response(mimetype='text/plain', template_file='seo/robots.txt')
def robots():
    return {}
