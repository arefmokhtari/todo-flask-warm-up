#   -   -   -   -   -   -   -   -   #
from .model import Model, db
#   -   -   -   -   -   -   -   -   #
class RunnerModel(Model):
    __tablename__ = 'runners'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255), nullable=False)
    cmd = db.Column(db.Text(), nullable=False)
    type = db.Column(db.String(15), nullable=False)
#   -   -   -   -   -   -   -   -   #