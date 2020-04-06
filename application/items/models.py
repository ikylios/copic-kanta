from application import db

from sqlalchemy.sql import text

class Item(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        name = db.Column(db.String(30), nullable=False)
        colorcode = db.Column(db.String(30), nullable=False)
        ptype = db.Column(db.String(30), nullable=False)
#        type_id = db.Column(db.Integer, ForeignKey('type.id') nullable=False)
#        ptype = relationship("Type", uselist=False)

        lowink = db.Column(db.Boolean, nullable=False)

        account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

        def __init__(self, name, colorcode, ptype):
                self.name = name
                self.ptype = ptype
                self.lowink = False
                self.colorcode = colorcode


        def get_id(self):
            return self.id

        def get_lowink(self):
            return self.lowink

        def get_name(self):
            return self.name

        @staticmethod
        def find_lowink():
                stmt = text("SELECT Item.colorcode, Item.name, Item.type"
                                " FROM Item WHERE Item.lowink = 1"
                                " GROUP BY Item.account_id")
                result = db.engine.execute(stmt)

                response = []
                for row in result:
                    response.append({"colorcode":row[0], "name":row[1], "type":row[2]})

                return response

        @staticmethod
        def in_masterlist(item):
                stmt = text("SELECT Item.id FROM Item WHERE Item.name = '{}' AND Item.colorcode = '{}' AND Item.ptype = '{}'".format(item.name, item.colorcode, item.ptype))
                result = db.engine.execute(stmt)

                response = []

                if not response:
                        return False

        @staticmethod
        def in_personallist(item):
            print("AAAAAAAAAAAAA")
            stmt = text("SELECT Item.id FROM Item WHERE Item.colorcode = '{}' AND Item.account_id = '{}'".format(item.colorcode, item.account_id))
            result = db.engine.execute(stmt)
            print(result)
            for row in res:
                print(row[0])
                print(row[1])
            print("EEEEE")
            resp = []
            for row in result:
                resp.append({row[0]})
            if not resp:
                return False
