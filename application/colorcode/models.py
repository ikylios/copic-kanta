from application import db

from sqlalchemy.sql import text

class Colorcode(db.Model):

        __tablename__ = "colorcode"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(30), nullable=False)
        code = db.Column(db.String(30), nullable=False)

        items = db.relationship("Item", backref="colorcode", lazy=True)

        def __init__(self, code, name):
                self.code = code
                self.name = name

        @staticmethod
        def colorcode_list():
                return Colorcode.query.order_by(Colorcode.code)

        @staticmethod
        def in_database(cc):
                stmt = text("SELECT Colorcode.code FROM Colorcode WHERE Colorcode.code = '{}'".format(cc.code))
                result = db.engine.execute(stmt)

                response = []

                if not response:
                        return False
