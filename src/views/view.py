#   -   -   -   -   -   -   -   -   #
from flask import request, jsonify, render_template
from flask.views import MethodView
from typing import Any
from json import loads as json_loads
#   -   -   -   -   -   -   -   -   #
class View(MethodView):
    #   -   -   -   -   #
    def response(self, data: Any, status_code: int = 200, **context):
        if type(data) == str:
            return self.tempate(data, **context)
        return jsonify(data), status_code
    #   -   -   -   -   #
    def _get_data(self, attr: str = 'values') -> dict:
        if attr == 'data':
            return json_loads(request.data)
        return dict(getattr(request, attr))
    #   -   -   -   -   #
    def tempate(self, name: str, **context):
        return render_template(f'{name}.html', **context)
    #   -   -   -   -   #
#   -   -   -   -   -   -   -   -   #
__all__ = [ 'View', ]
#   -   -   -   -   -   -   -   -   #