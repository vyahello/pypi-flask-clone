import flask

from pypi_org.infra.view_modifiers import response
from pypi_org.models.home.index import IndexViewModel
from pypi_org.models.shared.modelbase import ViewModelBase

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    vm = ViewModelBase()
    return vm.to_dict()
