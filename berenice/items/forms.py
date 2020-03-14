from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    pass
    make = StringField('make', validators=[DataRequired()], default='Ford')
    model = StringField('model', validators=[DataRequired()], default='Mustang')
    year = StringField('year', validators=[DataRequired()], default='2007')
    body_type = SelectField(
        choices=[
            ('0', 'Sedan'),('1', 'Compact'),
            ('2', 'Coupe'), ('3', 'Pickup'),
            ('4' ,'SUV')
            ], default='2')

    dest_id = SelectField(
        choices=[('0', 'Alabama'),('1', 'Baltimore'),
                 ('2', 'California'), ('3', 'Delaware'), ('4', 'Exeter')], default='0')
    ship_status = SelectField(
        choices=[
            ('0', 'not yet shipped'),
            ('1', 'receive next week'),
            ('2', 'receive following week'),
            ('3', 'receive within a month'),
            ('4', 'receive next month'),
        ], default='0'
    )


class ItemDemo():
    pass
    date_posted = datetime.utcnow

    def __init__(self, make='', model='', year='', body_type='', dest_id='', ship_status=''):
        pass

        self.make = make
        self.model = model
        self.year = year
        self.body_type = body_type
        self.dest_id = dest_id
        self.ship_status = ship_status


    def __repr__(self):
        return f"ItemDemo('\n...{self.make}'\n\t '{self.model}' \n\t '{self.year}')"


class ShipperDisplayForm(FlaskForm):
    pass

    make = StringField('make')
    model = StringField('model')
    year = StringField('year')
    body_type = SelectField(
        choices=[
            ('0', 'Sedan'), ('1', 'Compact'),
            ('2', 'Coupe'), ('3', 'Pickup'),
            ('4', 'SUV')
        ])
        
    destination = SelectField(
        choices=[('0', 'Alabama'), ('1', 'Baltimore'),
                 ('2', 'California'), ('3', 'Delaware'), ('4', 'Exeter')])

    ship_status = SelectField(
        choices=[
            ('0', 'not yet shipped'),
            ('1', 'receive next week'),
            ('2', 'receive following week'),
            ('3', 'receive within a month'),
            ('4', 'receive next month'),
        ]
    )
