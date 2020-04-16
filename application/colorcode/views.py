from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.colorcode.models import Cc_ptype

@app.route("/items/vproducts/", methods=["GET"])
@login_required(role="ADMIN")
def cc_ptype_index():
        return render_template("colorcode/list.html", items = Cc_ptype.list_products())
