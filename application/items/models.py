from application import db

from sqlalchemy.sql import text

class Item(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        lowink = db.Column(db.Boolean, nullable=False)
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

        account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
        colorcode_id = db.Column(db.Integer, db.ForeignKey('colorcode.id'), nullable=False)
        ptype_id = db.Column(db.Integer, db.ForeignKey('ptype.id'), nullable=False)

        def __init__(self):
            self.lowink = False

        def get_id(self):
            return self.id

        def get_lowink(self):
            return self.lowink

        def get_name(self):
            return self.name


        @staticmethod
        def general_index():
            stmt = text("SELECT Item.id, Colorcode.code, Colorcode.name, Ptype.name, Account.username "
                    " FROM Item" 
                    " JOIN Account ON Item.account_id = Account.id" 
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " ORDER BY Item.id DESC")
            res = db.engine.execute(stmt)

            response = []
            for row in res:
#                    print("row:" + str(row))
                response.append({"id":row[0], "colorcode":row[1], "colorname":row[2], "ptype":row[3], "username":row[4]})
#                    for x, y in response[0].items():
#                        print(x, y)
#                    print("res0:" + str(response[0]))
#                print("response: " + str(response)) 
            return response
    
        @staticmethod
        def personal_index(user_id):
            stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                    " FROM Item" 
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " ORDER BY Colorcode.code")
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                lowink_status = "No" 
                if row[3]:
                    lowink_status = "Yes"
                response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "lowink":lowink_status, "id":row[4]})
            return response

        @staticmethod
        def find_lowink(user_id):
            stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                    " FROM Item" 
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " AND Item.lowink = '1'"
                    " ORDER BY Colorcode.code")
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "lowink":"Yes", "id":row[4]})
            return response

        @staticmethod
        def most_popular_cc():
            stmt = text("SELECT Colorcode.code, Colorcode.name, COUNT(Colorcode.id)"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " GROUP BY Colorcode.id"
                    )
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"colorcode":row[0], "colorname":row[1], "number owned":row[2]})
            return response
    
        @staticmethod
        def most_popular():
            stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, COUNT(Colorcode.id) AS ccfreq, COUNT(Ptype.id) AS ptypefreq"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " GROUP BY Item.colorcode_id"
                    " ORDER BY ccfreq, ptypefreq"
                    )
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "nr of cc":row[3], "nr of ptype":row[4]})
            return response


        @staticmethod
        def codesearch(user_id, incl, searchterm):
            searchterm = searchterm.upper()
            if (searchterm == "W" or searchterm == "C"):
                searchterm += "-"

            condition = ""
            if incl:
                condition += "LIKE '%" + searchterm + "%'"
            else: 
                condition += "GLOB '" + searchterm + "[0-9]*'"
                if (searchterm == "0" or len(searchterm) >= 3):
                    condition = "LIKE '" + searchterm + "'" 

            stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " AND Colorcode.code " + condition +
                    " ORDER BY Colorcode.code")
            print("-------stmt:" + str(stmt))
            res = db.engine.execute(stmt)

            print(str(res)) 

            response = []
            for row in res:
                print("-----row:" + str(row))
                lowink_status = "No" 
                if row[3]:
                    lowink_status = "Yes"
                response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "lowink":lowink_status, "id":row[4]})
                
            return response


        @staticmethod
        def date_added(user_id):
            stmt = text("SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.date_created, Item.id"
                    " FROM Item" 
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " ORDER BY Item.date_created")
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                lowink_status = "No" 
                if row[3]:
                    lowink_status = "Yes"
                date = "" + row[4]
                date2 = date[0:10]
                date = date2[8:10] + date2[4:8] + date2[0:4]
                response.append({"colorcode":row[0], "colorname":row[1], "ptype":row[2], "lowink":lowink_status, "date_added":date, "id":row[5]})
            return response
