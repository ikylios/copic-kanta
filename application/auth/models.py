from application import db
from sqlalchemy import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    items = db.relationship("Item", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        if self.admin: return True
        return False

    def roles(self):
        if self.admin: 
            return ["ADMIN"]
        return ["USER"]


    @staticmethod
    def by_user():
            stmt = text("SELECT Account.username, COUNT(Item.id)"
                  " FROM Account"
                    " LEFT JOIN Item ON Account.id = Item.account_id"
                    " GROUP BY Account.id"
                    " ORDER BY COUNT(Item.id) DESC"
                    )
            res = db.engine.execute(stmt)

            response = []
            for row in res:
               response.append({"username":row[0], "number owned":row[1]})
            return response


