from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.items.models import Item

from application.colorcode.models import Cc_ptype
from application.colorcode.models import Colorcode
from application.colorcode.forms import Cc_ptypeForm

from application.ptype.models import Ptype

@app.route("/items/vproducts/", methods=["GET"])
@login_required(role="ADMIN")
def cc_ptype_index():
        return render_template("colorcode/list.html", items = Cc_ptype.list_products())

@app.route("/items/vproducts/delete/<ccid>/<ptypeid>", methods=["POST"])
@login_required(role="ADMIN")
def cc_ptype_delete(ccid, ptypeid):
    
    cc_ptype = Cc_ptype.query.filter(Cc_ptype.colorcode_id == ccid, Cc_ptype.ptype_id == ptypeid).first()
    
    items = Item.query.filter(Item.colorcode_id == cc_ptype.colorcode_id, Item.ptype_id == cc_ptype.ptype_id)

    for item in items:
        db.session.delete(item)

    db.session.delete(cc_ptype)
    
    db.session().commit()

    return redirect(url_for("cc_ptype_index"))


@app.route("/items/vproducts/new", methods=["GET", "POST"])
@login_required(role="ADMIN")
def cc_ptype_form(): 
   
    form = Cc_ptypeForm(request.form)
    
    if request.method == "GET":
        return render_template("colorcode/new.html", form = form)
    
    if not form.validate():
        return render_template("colorcode/new.html", form = form)
    
    cc = Colorcode.query.filter(Colorcode.code == form.colorcode.data).first()
    if not cc:
        cc = Colorcode(form.colorcode.data, form.name.data)
        db.session.add(cc)

    ptype = Ptype.query.filter(Ptype.name == form.ptype.data.name).first()

    duplicate = Cc_ptype.query.filter(Cc_ptype.colorcode_id == cc.id, Cc_ptype.ptype_id == ptype.id).first()
    if duplicate:
        return render_template("colorcode/new.html", form = form, error = "Product already in database.")

    ccptype = Cc_ptype(cc.id, ptype.id)
    db.session.add(ccptype)
    
    db.session().commit()
    return redirect(url_for("cc_ptype_index"))

