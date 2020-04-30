from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.items.models import Item
from application.items.forms import ItemForm
from application.items.forms import CodeSearchForm

from application.colorcode.models import Cc_ptype
from application.colorcode.models import Colorcode
from application.colorcode.forms import CcForm

from application.ptype.models import Ptype
from application.ptype.forms import PtypeForm

@app.route("/products/", methods=["GET"])
def cc_ptype_index():
        return render_template("colorcode/list.html", items = Cc_ptype.list_products(), form = CodeSearchForm())

@app.route("/products/cc", methods=["GET"])
def cc_only():
    if not current_user.is_anonymous:
        if "ADMIN" in current_user.roles():
            return render_template("colorcode/listwdelete.html", items = Colorcode.cc_iterable(), form = CodeSearchForm())
    return render_template("colorcode/listccptype.html", items = Colorcode.cc_iterable(), form = CodeSearchForm())


@app.route("/products/ptype", methods=["GET"])
def ptype_only():
    if not current_user.is_anonymous:
        if "ADMIN" in current_user.roles():
            return render_template("colorcode/listwdelete.html", items = Ptype.ptype_iterable(), form = CodeSearchForm())
    return render_template("colorcode/listccptype.html", items = Ptype.ptype_iterable(), form = CodeSearchForm())

@app.route("/products/most_cc/", methods=["GET"])
def most_popular_cc():
    return render_template("colorcode/listwdelete.html", items = Colorcode.most_popular_cc(), form = CodeSearchForm())


@app.route("/products/delete/<ccid>/<ptypeid>", methods=["POST"])
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

@app.route("/products/delete/cc/<ccid>", methods=["POST"])
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

@app.route("/products/delete/ptype/<ptypeid>", methods=["POST"])
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


@app.route("/products/codesearch", methods=["POST"])
def cc_codesearch():

    form = CodeSearchForm(request.form)

    if not form.validate():
        return render_template("colorcode/listwdelete.html", form = form, error = "Invalid code")

    return render_template("colorcode/listwdelete.html", items = Cc_ptype.codesearch_cc(form.incl.data, form.search.data), form = CodeSearchForm())


@app.route("/addtodb", methods=["GET"])
@login_required(role="ADMIN")
def db_form():
    return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = PtypeForm())



@app.route("/product/new", methods=["POST"])
@login_required(role="ADMIN")
def cc_ptype_form(): 
   
    form = ItemForm(request.form)
    
    if not form.validate():
        return render_template("dbnew.html", formItem = form, formCc = CcForm(), formPtype = PtypeForm())
    
    cc = Colorcode.query.filter(Colorcode.code == form.colorcode.data.code).first()
    ptype = Ptype.query.filter(Ptype.name == form.ptype.data.name).first()

    duplicate = Cc_ptype.query.filter(Cc_ptype.colorcode_id == cc.id, Cc_ptype.ptype_id == ptype.id).first()
    if duplicate:
        return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = PtypeForm(), errorItem = "Product already in database.")

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

    duplicate = Colorcode.query.filter(Colorcode.code == form.code.data).first()
    if duplicate:
        return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = PtypeForm(), errorCc = "Colorcode already in database.")

    cc = Colorcode(form.code.data, form.name.data)

    db.session().add(cc)
    db.session().commit()

    return redirect(url_for("cc_only"))


@app.route("/ptype/new/", methods=["POST"])
@login_required(role="ADMIN")
def ptype_form():

    form = PtypeForm(request.form)

    if not form.validate():
        return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = form)

    duplicate = Ptype.query.filter_by(name=form.pname.data).first()
    if duplicate:
        return render_template("dbnew.html", formItem = ItemForm(), formCc = CcForm(), formPtype = PtypeForm(), errorPtype = "Product type already in database.")

    ptype = Ptype(form.pname.data)

    db.session().add(ptype)
    db.session().commit()

    return redirect(url_for("ptype_only"))

