
from application import db

class Ptype(db.Model):

    __tablename__ = "ptype"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)

    items = db.relationship("Item", backref="ptype", lazy=True, cascade="all, delete-orphan")
    colorcodes = db.relationship("Cc_ptype", back_populates="ptype", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def ptype_list():
        return Ptype.query.order_by(Ptype.name)

