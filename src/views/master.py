#   -   -   -   -   -   -   -   -   #
from ..models import MasterModel
from .view import View
from flask import Blueprint
from flask import redirect, make_response
from ..config import TOKEN_NAME, MASTER_PASSWORD
from ..decorators.auth import auth
from datetime import timedelta, datetime as dt
#   -   -   -   -   -   -   -   -   #
class RunnerView(View):
    def login(self):
        return self.response('login')

    def login_form(self):
        data = self._get_data()
        master: MasterModel = MasterModel.query.filter_by(username=data.get('username'),).first()
        if not master or not master.check_password(data['password']):
            return self.response('login', error='username or password is wrong!',)
        response = make_response(redirect('/runner'))
        response.set_cookie(TOKEN_NAME, master.token, expires=dt.now() + timedelta(1))
        return response

    @auth
    def logout(self):
        response = make_response(self.response({
            'message': 'ok',
            'data': 'bye master!',
        }))
        response.delete_cookie(TOKEN_NAME)
        return response
    
    def create_master(self):
        MasterModel.create_master(
            'plagu3dr',
            MASTER_PASSWORD,
        )
        return self.response({
            'message': 'ok',
        })
#   -   -   -   -   -   -   -   -   #
blueprint = Blueprint('master', __name__)
blueprint.add_url_rule('/login', view_func=RunnerView().login, methods=['GET'],)
blueprint.add_url_rule('/login', view_func=RunnerView().login_form, methods=['POST'],)
blueprint.add_url_rule('/leave-master', view_func=RunnerView().logout, methods=['POST'],)
blueprint.add_url_rule('/create-master', view_func=RunnerView().create_master, methods=['GET',],)
#   -   -   -   -   -   -   -   -   #