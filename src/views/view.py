#   -   -   -   -   -   -   -   -   #
from flask import request, jsonify, render_template, Blueprint as BaseBlueprint
from flask.views import MethodView
from typing import Any
#   -   -   -   -   -   -   -   -   #
class View(MethodView):
    #   -   -   -   -   #
    def response(self, data: Any, status_code: int = 200):
        if isinstance(data, tuple):
            return self.tempate(*data)
        if isinstance(data, str):
            return self.tempate(data)
        return jsonify(data), status_code
    #   -   -   -   -   #
    def _get_data(self, attr: str = 'values'):
        return getattr(request, attr)
    #   -   -   -   -   #
    def tempate(self, name: str, **context):
        return render_template(f'{name}.html', **context)
    #   -   -   -   -   #
#   -   -   -   -   -   -   -   -   #
__all__ = [ 'Controller', ]
#   -   -   -   -   -   -   -   -   #