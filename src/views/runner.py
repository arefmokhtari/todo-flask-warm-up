#   -   -   -   -   -   -   -   -   #
from .view import View
from ..decorators.blueprint import blueprint, route
from ..models import RunnerModel
from ..decorators.auth import auth
from subprocess import run as subprocess_run
#   -   -   -   -   -   -   -   -   #
@blueprint(__name__)
class RunnerView(View):
    @auth
    @route('/runner')
    def get(self):
        runners = RunnerModel.query.all()
        return self.response('runner', runners=runners)

    @auth
    @route('/runner', 'post',)
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