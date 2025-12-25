#   -   -   -   -   -   -   -   -   #
from .view import View
from ..decorators.blueprint import blueprint, route
#   -   -   -   -   -   -   -   -   #

@blueprint(__name__)
class IndexView(View):
    @route('/')
    def index(self):
        return self.response('index')
    
#   -   -   -   -   -   -   -   -   #