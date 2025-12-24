#   -   -   -   -   -   -   -   -   #
from .view import View
from flask import Blueprint
from ..models import RunnerModel
from ..decorators.auth import auth
from subprocess import run as subprocess_run
#   -   -   -   -   -   -   -   -   #
class RunnerView(View):
    @auth
    def get(self):
        runners = RunnerModel.query.all()
        print(runners)
        return self.response('runner', runners=runners)

    @auth
    def post(self):
        data = self._get_data('data')
        cmd = data.get('cmd')
        result = subprocess_run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            data = {
                'cmd': cmd,
                'data': result.stdout,
                'type': 'stdout',
            }
        else:
            data = {
                'cmd': cmd,
                'data': result.stderr,
                'type': 'stderr',
            }
        print(data)
        runner = RunnerModel(**data)
        runner.save()

        return self.response(data)

#   -   -   -   -   -   -   -   -   #
blueprint = Blueprint('runner', __name__,)
blueprint.add_url_rule('/runner', view_func=RunnerView.as_view('get'), methods=['GET'])
blueprint.add_url_rule('/runner', view_func=RunnerView.as_view('post'), methods=['POST',],)
#   -   -   -   -   -   -   -   -   #