from flask import (
    render_template, url_for, flash,
    redirect, request, abort, Blueprint
)
from flask_login import (
    current_user, login_required
)
from berenice import db
from berenice.models import (
    User, Item
)
from berenice.items.forms import (
    ItemForm, ItemDemo, ShipperDisplayForm
)
items = Blueprint('items', __name__)


@items.route("/shipper/home", methods=['GET', 'POST'])
@login_required
def shipper_home():
    pass
    form = ShipperDisplayForm()
    inventory = Item.query.all()
    try:
        _ = [item for item in inventory]
    except:
        inventory = []
    if request.method == 'POST':
        pass
        inventory = Item.query.filter_by(
            dest_id=str(request.form["destination"])).all()
        inventory = [
            item for item in inventory
        ]

        return render_template(
            'shipper_home.html',
            form=form,
            inventory=inventory,
            title='ShipperDispLoc'
            )
    return render_template(
        'shipper_home.html',
        form=form,
        inventory=inventory,
        title='ShipperHome'
        )



@items.route("/h0me/<int:my_location_id>")
@login_required
def displayMyCarsOnly(my_location_id):
    pass
    inventory = Item.query.filter_by(dest_id=str(my_location_id)).all()
    inventory = [
        item for item in inventory
    ]

    print(inventory)

    return render_template('h0me.html', inventory=inventory, title='My Cars')

@items.route("/h0me")
@login_required
def h0me():
    pass
    inventory = Item.query.all()

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
            make=request.form["make"],
            model=request.form["model"],
            year=request.form["year"],
            body_type=request.form["body_type"],
            dest_id=request.form["dest_id"],
            ship_status=request.form["ship_status"],
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
                 body_type=_bodyType, dest_id=_destId, ship_status=_shipStatus)
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
            ['2011', '2012', '2013', '2014', '2015', ],
            ['0', '1', '2', '3', '4', ],
            ['0', '1', '2', '3', '4', ],
            ['0', '1', '2', '3', '4', ])]

    return dict(ItemDemoList=ItemDemoList)


@items.context_processor
def inject_destStyleDict():
    pass
    def destStyler(item_dest_index):
        pass
        destStyleDict = {
            '0': 'danger',
            '1': 'warning',
            '2': 'success',
            '3': 'info',
            '4': 'primary',
            '99': 'secondary',
        }
        return destStyleDict.get(item_dest_index, 'secondary')
        
    return dict(destStyler=destStyler)




@items.context_processor
def inject_bodyTypeImgDict():
    pass

    def imageFinder(item_bodyType_index):
        pass
        bodyTypeImgDict = {
            '0': '00.png',
            '1': '01.png',
            '2': '02.png',
            '3': '03.png',
            '4': '04.png',
        }
        return bodyTypeImgDict.get(item_bodyType_index,'00.png')

    return dict(imageFinder=imageFinder)


@items.context_processor
def inject_bodyTypeTextDict():
    pass
    def typeFinder(item_bodyType_id):
        pass
        bodyTypeTextDict = {
        '0': 'Sedan',
        '1': 'Compact',
        '2': 'Coupe',
        '3': 'Pickup',
        '4': 'SUV',
        }
        return bodyTypeTextDict.get(item_bodyType_id, 'UnknownBodyType')

    return dict(typeFinder=typeFinder)


@items.context_processor
def inject_shipStatMsgDict():
    pass
    def statusFinder(item_ship_status):
        pass
        shipStatMsgDict = {
            '0': 'not yet shipped',
            '1': 'receive next week',
            '2': 'receive following week',
            '3': 'receive within a month',
            '4': 'receive next month',
        }
        return shipStatMsgDict.get(item_ship_status, 'UnknownShipmentStatus')
    
    return dict(statusFinder=statusFinder)
 

@items.context_processor
def inject_destCityDict():
    pass
    def cityFinder(item_dest_id):
        pass
        destCityNameDict = {
            '0': 'Alabama',
            '1': 'Baltimore',
            '2': 'California',
            '3': 'Delaware',
            '4': 'Exeter',
        }
        return destCityNameDict.get(item_dest_id, 'UnknownDestinationCity')
    return dict(cityFinder=cityFinder)

