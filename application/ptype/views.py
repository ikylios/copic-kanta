from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.ptype.models import Ptype
from application.ptype.forms import PtypeForm


@app.route("/ptype/new/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def ptype_form():
    if request.method == "GET":
        return render_template("ptype/new.html", form = PtypeForm())

    form = PtypeForm(request.form)

    if not form.validate():
       return render_template("ptype/new.html", form = form)

    qptype = Ptype.query.filter_by(name=form.name.data).first()
    if qptype:
        return render_template("ptype/new.html", form = form, error = "Product type already in database.")

    ptype = Ptype(form.name.data)

    db.session().add(ptype)
    db.session().commit()

    return redirect(url_for("items_index"))

