#   -   -   -   -   -   -   -   -   #
from flask import request, redirect, g
from functools import update_wrapper
from ..models.master import MasterModel
from ..config import TOKEN_NAME
#   -   -   -   -   -   -   -   -   #

def auth(f):
    def wrapper(*args, **kwargs):
        token = request.cookies.get(TOKEN_NAME, None)
        master: MasterModel = MasterModel.query.filter_by(token=token).first()
        if not master:
            return redirect('/login')
        g.master = master
        return f(*args, **kwargs)

    return update_wrapper(wrapper, f)
#   -   -   -   -   -   -   -   -   #