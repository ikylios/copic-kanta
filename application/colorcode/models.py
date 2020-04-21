from application import db

from sqlalchemy.sql import text

class Colorcode(db.Model):

        __tablename__ = "colorcode"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(30), nullable=False)
        code = db.Column(db.String(30), nullable=False)

        items = db.relationship("Item", backref="colorcode", lazy=True, cascade="all, delete-orphan")
        ptypes = db.relationship("Cc_ptype", back_populates="colorcode", cascade="all, delete-orphan")

        def __init__(self, code, name):
                self.code = code
                self.name = name

        @staticmethod
        def colorcode_list():
                return Colorcode.query.order_by(Colorcode.code)

        @staticmethod
        def cc_iterable():
                stmt = text("SELECT Colorcode.id, Colorcode.code, Colorcode.name" 
                        " FROM Colorcode")
                res = db.engine.execute(stmt)

                response = []
                for row in res:
                    response.append({"ccid":row[0], "colorcode":row[1], "colorname":row[2]})
                return response




class Cc_ptype(db.Model):

    __tablename__ = "cc_ptype"

    colorcode_id = db.Column(db.Integer, db.ForeignKey("colorcode.id"), primary_key=True, nullable=False)
    ptype_id = db.Column(db.Integer, db.ForeignKey("ptype.id"), primary_key=True, nullable=False)

    colorcode = db.relationship("Colorcode", back_populates="ptypes")
    ptype = db.relationship("Ptype", back_populates="colorcodes")

    def __init__(self, colorcode_id, ptype_id):
        self.colorcode_id = colorcode_id
        self.ptype_id = ptype_id

    @staticmethod
    def list_products():
                stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, Colorcode.id, Ptype.id"
                        " FROM Cc_ptype"
                        " JOIN Colorcode ON Cc_ptype.colorcode_id = Colorcode.id"
                        " JOIN Ptype ON Cc_ptype.ptype_id = Ptype.id"
                        " ORDER BY Colorcode.code")
                res = db.engine.execute(stmt)

                response = []
                for row in res:
                    response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "ccid":row[3], "ptypeid":row[4]})
                return response

