
from application import db

class Ptype(db.Model):

    __tablename__ = "ptype"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name

    @staticmethod
    def ptype_list():
        return Ptype.query

