
from application import db

class Ptype(db.Model):

    __tablename__ = "ptype"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)

    items = db.relationship("Item", backref="ptype", lazy=True)


    def __init__(self, name):
        self.name = name

    @staticmethod
    def ptype_list():
        return Ptype.query.order_by(Ptype.name)

