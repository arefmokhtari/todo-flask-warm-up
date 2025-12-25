#   -   -   -   -   -   -   -   -   #
from ..models import MasterModel
from .view import View
from flask import redirect, make_response
from ..config import TOKEN_NAME, MASTER_PASSWORD
from ..decorators.auth import auth
from datetime import timedelta, datetime as dt
from ..decorators.blueprint import blueprint, route
#   -   -   -   -   -   -   -   -   #
@blueprint(__name__)
class MasterView(View):
    @route('/login')
    def login(self):
        return self.response('login')

    @route('/login', 'post')
    def login_form(self):
        data = self._get_data()
        master: MasterModel = MasterModel.query.filter_by(username=data.get('username'),).first()
        if not master or not master.check_password(data['password']):
            return self.response('login', error='username or password is wrong!',)
        response = make_response(redirect('/runner'))
        response.set_cookie(TOKEN_NAME, master.token, expires=dt.now() + timedelta(1))
        return response

    @auth
    @route('/leave-master', 'post')
    def logout(self):
        response = make_response(self.response({
            'message': 'ok',
            'data': 'bye master!',
        }))
        response.delete_cookie(TOKEN_NAME)
        return response
    
    # @route('/create-master')
    def create_master(self):
        MasterModel.create_master(
            'plagu3dr',
            MASTER_PASSWORD,
        )
        return self.response({
            'message': 'ok',
        })
#   -   -   -   -   -   -   -   -   #