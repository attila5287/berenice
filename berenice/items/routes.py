from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from berenice import db
from berenice.models import User, Item
from berenice.items.forms import  ItemForm, ItemDemo


items = Blueprint('items', __name__)


@items.route("/h0me")
def h0me():
    pass
    page = request.args.get('page', 1, type=int)
    inventory = Item.query.order_by(
        Item.date_posted.desc()).paginate(page=page, per_page=5)

    try:
        _ = [item for item in inventory]
    except:
        inventory = []
    return render_template('h0me.html', inventory=inventory, title='My Cars')

@items.route("/item/new", methods=['GET', 'POST'])
@login_required
def new_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(
            make = request.form["make"], 
            model = request.form["model"], 
            year = request.form["year"],     
            body_type = request.form["body_type"],     
            dest_id = request.form["dest_id"],     
            ship_status = request.form["ship_status"], 
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added to inventory!', 'success')
        return redirect(url_for('items.h0me'))
    return render_template('create_item.html', title='New Item',
                           form=form, legend='New Item')



@items.context_processor
def inject_ItemDemoList():
    pass
    ItemDemoList = [
        ItemDemo(make=_make, model=_model, year=_year,
                 bodyType=_bodyType, destId=_destId, shipStatus=_shipStatus)
                 for (_make, _model, _year, _bodyType, _destId, _shipStatus) in
                 zip(
                     [
                         'Chrysler',
                         'Mini',
                         'Ford',
                         'Toyota',
                         'Hummer',
                     ],
                     [
                         '300',
                         'Cooper',
                         'Mustang',
                         'TRD',
                         'H3',
                     ],
                     ['2011', '2012', '2013', '2014', '2015',],
                     ['00.png', '01.png', '02.png', '03.png', '04.png', ],
                     ['info', 'warning', 'success', 'danger', 'fifth', ],
                     ['0', '1', '2', '0', '1',])]
        
    return dict(ItemDemoList=ItemDemoList)
