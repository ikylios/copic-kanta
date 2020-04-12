from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.items.models import Item
from application.items.forms import ItemForm, PersonalItemForm

from application.colorcode.models import Colorcode
from application.ptype.models import Ptype

from application.auth.models import User

@app.route("/items/", methods=["GET"])
@login_required(role="ADMIN")
def items_index():
#	return render_template("items/withusernames.html", items = Item.query.all(), users = User.with_username())
        return render_template("items/list.html", items = Item.query.all())

@app.route("/items/myitems/", methods=["GET"])
@login_required
def items_myindex():
        return render_template("items/listpersonal.html", items =
               Item.query.filter(Item.account_id == current_user.id))


@app.route("/items/myitems/lowink/", methods=["GET"])
def items_lowink():
	return render_template("items/listpersonal.html", items =
		Item.query.filter(Item.lowink == True, Item.account_id == current_user.id)) 

@app.route("/items/most/", methods=["GET"])
def items_most():
        return render_template("items/list.html", items = Item.query.all())

@app.route("/items/myitems/setink/<item_id>/", methods=["POST"])
@login_required
def items_set_lowink(item_id):

    item = Item.query.get(item_id)
    if item.lowink == True:
        item.lowink = False
    else:
        item.lowink = True

    db.session().commit()

    return redirect(url_for("items_myindex"))


@app.route("/items/delete/<item_id>/", methods=["POST"])
@login_required
def items_delete(item_id):

    item = Item.query.get(item_id)

    if item.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session.delete(item)
    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/new/general", methods=["GET", "POST"])
@login_required(role="ADMIN")
def items_form():
    form = ItemForm(request.form)
    
    if request.method == "GET":
        return render_template("items/new.html", form = form)

    if not form.validate():
       return render_template("items/new.html", form = form)
    
    qcc = Colorcode.query.filter(Colorcode.code == form.colorcode.data).first()
    if not qcc:
        cc = Colorcode(form.colorcode.data)    
        db.session.add(cc)

    qitem = Item.query.filter(Item.name == form.name.data, Item.colorcode == form.colorcode.data, Item.ptype == form.ptype.data.name).first()
    if qitem:
        return render_template("items/new.html", form = form, error = "Product already in database.")

    item = Item(form.name.data, form.colorcode.data, form.ptype.data.name)
    item.lowink = False
    item.account_id = current_user.id       

    db.session.add(item)  
    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/new/personal/", methods=["GET", "POST"])
@login_required
def personal_items_form():
    if request.method == "GET":
        return render_template("items/personal.html", form = PersonalItemForm())

    form = PersonalItemForm(request.form)

    if not form.validate():
       return render_template("items/personal.html", form = form)

    cc = Colorcode.query.filter(Colorcode.code == form.colorcode.data.code).first()

    validProduct = Item.query.filter(Item.colorcode == form.colorcode.data.code, Item.ptype == form.ptype.data.name).first()

    if not validProduct:
        return render_template("items/personal.html", form = form,
                               error = "Product does not exist.")

    duplicate = Item.query.filter(Item.colorcode == form.colorcode.data.code, Item.ptype == form.ptype.data.name, Item.account_id == current_user.id).first()

    if duplicate:
        return render_template("items/personal.html", form = form,
                               error = "Product already in collection.")
        
   
    itname = Item.query.filter_by(colorcode=form.colorcode.data.code).first().get_name()
    item = Item(itname, form.colorcode.data.code, form.ptype.data.name)
    item.account_id = current_user.id

    db.session.add(item)
    db.session().commit()

    return redirect(url_for("items_index"))
