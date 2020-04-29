from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.items.models import Item
from application.items.forms import ItemForm, CodeSearchForm

from application.colorcode.models import Colorcode
from application.ptype.models import Ptype

from application.colorcode.models import Cc_ptype

from application.auth.models import User


@app.route("/", methods=["GET"])
@login_required
def index():
    if "ADMIN" in current_user.roles():
       return redirect(url_for("items_index"))

    return redirect(url_for("items_myindex"))

 
@app.route("/items/", methods=["GET"])
@login_required(role="ADMIN")
def items_index():
        return render_template("items/list.html", general_index = Item.general_index())

@app.route("/items/myitems/", methods=["GET"])
@login_required(role="USER")
def items_myindex():
    return render_template("items/listpersonal.html", items = Item.personal_index(str(current_user.id)), form = CodeSearchForm())


@app.route("/items/myitems/lowink/", methods=["GET"])
def items_lowink():
    return render_template("items/listpersonal.html", items = Item.find_lowink(str(current_user.id)), form = CodeSearchForm())


@app.route("/items/most/", methods=["GET"])
@login_required(role="ADMIN")
def items_most_popular():
    return render_template("items/list.html", general_index = Item.most_popular())

@app.route("/items/most_cc/", methods=["GET"])
@login_required
def items_most_popular_cc():
    return render_template("colorcode/listdeleteifid.html", items = Colorcode.most_popular_cc())

@app.route("/items/by_user/", methods=["GET"])
@login_required(role="ADMIN")
def items_by_user():
    return render_template("items/list.html", general_index = User.by_user())

@app.route("/items/myitems/date", methods=["GET"])
@login_required(role="USER")
def items_date_added():
    return render_template("items/listpersonal.html", items = Item.date_added(str(current_user.id)), form = CodeSearchForm())


@app.route("/items/myitems/setink/<item_id>/", methods=["POST"])
@login_required
def items_set_lowink(item_id):

    item = Item.query.get(item_id)
    if item.lowink == True:
        item.lowink = False
    else:
        item.lowink = True

    db.session().commit()

    return redirect(url_for("index"))


@app.route("/items/delete/<item_id>/", methods=["POST"])
@login_required
def items_delete(item_id):
    
    owned = Item.query.filter(Item.id == item_id, Item.account_id == current_user.id).first()
    if owned:
        item = Item.query.get(item_id)
        db.session.delete(item)
        db.session().commit()

    return redirect(url_for("index"))


@app.route("/items/myitems/codesearch", methods=["POST"])
@login_required(role="USER")
def item_codesearch():

    form = CodeSearchForm(request.form)
    
    if not form.validate():
        return render_template("items/listpersonal.html", form = form, error = "Invalid code")
   
    return render_template("items/listpersonal.html", items = Item.codesearch(str(current_user.id), form.incl.data, form.search.data), form = CodeSearchForm())


@app.route("/items/myitems/new", methods=["GET", "POST"])
@login_required
def item_form():

    form = ItemForm(request.form)
    
    if request.method == "GET":
        return render_template("items/new.html", form = form)
    
    if not form.validate():
       return render_template("items/new.html", form = form)

    cc = Colorcode.query.filter(Colorcode.code == form.colorcode.data.code).first()
    ptype = Ptype.query.filter(Ptype.name == form.ptype.data.name).first()

    validProduct = Cc_ptype.query.filter(Cc_ptype.colorcode_id == cc.id, Cc_ptype.ptype_id == ptype.id).first()
    if not validProduct:
        return render_template("items/new.html", form = form,
                               error = "Product does not exist.")

    duplicate = Item.query.filter(Item.colorcode_id == cc.id, Item.ptype_id == ptype.id, Item.account_id == current_user.id).first()

    if duplicate:
        return render_template("items/new.html", form = form,
                               error = "Product already in collection.")
        
    item = Item()
    item.colorcode_id = cc.id
    item.ptype_id = ptype.id
    item.account_id = current_user.id

    db.session.add(item)
    db.session().commit()

    return redirect(url_for("index"))
