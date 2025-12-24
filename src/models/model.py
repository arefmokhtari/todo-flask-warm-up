#   -   -   -   -   -   -   -   -   #
from flask_sqlalchemy import SQLAlchemy
from ..app import app
#   -   -   -   -   -   -   -   -   #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#   -   -   -   -   -   -   -   -   #
db = SQLAlchemy(app)
#   -   -   -   -   -   -   -   -   #
class Model(db.Model):
    __abstract__ = True
    def save(self):
        db.session.add(self) 
        db.session.commit()
#   -   -   -   -   -   -   -   -   #
__all__ = [ 'db', ]