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

dash_app = Blueprint('dash_app', __name__)


@dash_app.route("/dash/home", methods=['GET', 'POST'])
@login_required
def shipper_home():
    pass
    form = ShipperDisplayForm()
    inventory = Item.query.all()
    try:
        _ = [item for item in inventory]
    except:
        inventory = []


    return render_template(
        'dash_shipperHome.html',
        inventory=inventory,
        title='ShipperHome'
    )
