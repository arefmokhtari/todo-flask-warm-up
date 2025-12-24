#   -   -   -   -   -   -   -   -   #
from .view import View
from flask import Blueprint
#   -   -   -   -   -   -   -   -   #

class IndexView(View):
    def index(self):
        return self.response('index')

#   -   -   -   -   -   -   -   -   #
blueprint = Blueprint('index', __name__)
blueprint.add_url_rule('/', view_func=IndexView().index, methods=['GET',],)
#   -   -   -   -   -   -   -   -   #