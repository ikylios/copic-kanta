from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.items.models import Item
from application.items.forms import ItemForm

from application.colorcode.models import Cc_ptype
from application.colorcode.models import Colorcode
from application.colorcode.forms import CcForm

from application.ptype.models import Ptype
from application.ptype.forms import PtypeForm

@app.route("/items/vproducts/", methods=["GET"])
@login_required(role="ADMIN")
def cc_ptype_index():
        return render_template("colorcode/list.html", items = Cc_ptype.list_products())

@app.route("/items/vproducts/cc", methods=["GET"])
@login_required(role="ADMIN")
def cc_only():
        return render_template("colorcode/listiterable.html", items = Colorcode.cc_iterable())

@app.route("/items/vproducts/ptype", methods=["GET"])
@login_required(role="ADMIN")
def ptype_only():
        return render_template("colorcode/listiterable.html", items = Ptype.ptype_iterable())



@app.route("/items/vproducts/delete/<ccid>/<ptypeid>", methods=["POST"])
@login_required(role="ADMIN")
def cc_ptype_delete(ccid, ptypeid):
    
    cc_ptype = Cc_ptype.query.filter(Cc_ptype.colorcode_id == ccid, Cc_ptype.ptype_id == ptypeid).first()
    
    items = Item.query.filter(Item.colorcode_id == cc_ptype.colorcode_id, Item.ptype_id == cc_ptype.ptype_id)

    for item in items:
        db.session.delete(item)

    db.session.delete(cc_ptype)

    ccHasProducts = Cc_ptype.query.filter(Cc_ptype.colorcode_id == ccid).first()
    if not ccHasProducts:
        cc = Colorcode.query.get(ccid)
        db.session.delete(cc)

    productHasColorcode = Cc_ptype.query.filter(Cc_ptype.ptype_id == ptypeid).first()
    if not productHasColorcode:
        ptype = Ptype.query.get(ptypeid)
        db.session.delete(ptype)
    
    db.session().commit()

    return redirect(url_for("cc_ptype_index"))

@app.route("/items/vproducts/delete/cc/<ccid>", methods=["POST"])
@login_required(role="ADMIN")
def cc_delete(ccid):
    
    cc_ptypes = Cc_ptype.query.filter(Cc_ptype.colorcode_id == ccid)

    for cc_ptype in cc_ptypes:
        db.session.delete(cc_ptype)
    
    items = Item.query.filter(Item.colorcode_id == ccid)

    for item in items:
        db.session.delete(item)

    cc = Colorcode.query.get(ccid)
    db.session.delete(cc)
    
    db.session().commit()

    return redirect(url_for("cc_only"))

@app.route("/items/vproducts/delete/ptype/<ptypeid>", methods=["POST"])
@login_required(role="ADMIN")
def ptype_delete(ptypeid):
    
    cc_ptypes = Cc_ptype.query.filter(Cc_ptype.ptype_id == ptypeid)

    for cc_ptype in cc_ptypes:
        db.session.delete(cc_ptype)
    
    items = Item.query.filter(Item.ptype_id == ptypeid)

    for item in items:
        db.session.delete(item)

    ptype = Ptype.query.get(ptypeid)
    db.session.delete(ptype)
    
    db.session().commit()

    return redirect(url_for("ptype_only"))


@app.route("/items/addtodb/", methods=["GET"])
@login_required(role="ADMIN")
def db_form():
    return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = PtypeForm())



@app.route("/items/vproducts/new", methods=["POST"])
@login_required(role="ADMIN")
def cc_ptype_form(): 
   
    form = ItemForm(request.form)
    
    if not form.validate():
        return render_template("dbnew.html", formItem = form, formCc = CcForm(), formPtype = PtypeForm())
    
    cc = Colorcode.query.filter(Colorcode.code == form.colorcode.data.code).first()
    ptype = Ptype.query.filter(Ptype.name == form.ptype.data.name).first()

    duplicate = Cc_ptype.query.filter(Cc_ptype.colorcode_id == cc.id, Cc_ptype.ptype_id == ptype.id).first()
    if duplicate:
        return render_template("dbnew.html", form = form, error = "Product already in database.")

    ccptype = Cc_ptype(cc.id, ptype.id)
    db.session.add(ccptype)
    
    db.session().commit()
    return redirect(url_for("cc_ptype_index"))



@app.route("/cc/new/", methods=["POST"])
@login_required(role="ADMIN")
def cc_form():

    form = CcForm(request.form)

    if not form.validate():
        return render_template("dbnew.html", formItem = ItemForm(), formCc = form, formPtype = PtypeForm())

    duplicate = Colorcode.query.filter_by(name=form.code.data).first()
    if duplicate:
        return render_template("dbnew.html", form = form, error = "Product type already in database.")

    cc = Colorcode(form.code.data, form.name.data)

    db.session().add(cc)
    db.session().commit()

    return redirect(url_for("cc_only"))

