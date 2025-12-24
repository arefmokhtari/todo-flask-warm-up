#   -   -   -   -   -   -   -   -   #
from .model import db, Model
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
#   -   -   -   -   -   -   -   -   #
class MasterModel(Model):
    __tablename__ = 'masters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False) 
    token = db.Column(db.String(50), unique=True, index=True)

    def set_password(self, password: str): 
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool: 
        return check_password_hash(self.password, password) 

    def generate_token(self): 
        self.token = secrets.token_hex(32)

    @classmethod
    def create_master(cls, username: str, password: str):
        master = cls(username=username)
        master.set_password(password)
        master.generate_token()
        master.save()
        return master
#   -   -   -   -   -   -   -   -   #

#   -   -   -   -   -   -   -   -   #