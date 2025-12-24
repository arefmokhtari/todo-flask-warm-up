#   -   -   -   -   -   -   -   -   #

from .model import app, db
from .runner import RunnerModel
from .master import MasterModel
#   -   -   -   -   -   -   -   -   #

with app.app_context():
    db.create_all()

#   -   -   -   -   -   -   -   -   #
