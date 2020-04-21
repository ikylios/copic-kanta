
from application import db

from sqlalchemy.sql import text


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

    @staticmethod
    def ptype_iterable():
                stmt = text("SELECT Ptype.id, Ptype.name"
                        " FROM Ptype")
                res = db.engine.execute(stmt)

                response = []
                for row in res:
                    response.append({"ptypeid":row[0], "ptype":row[1]})
                return response


