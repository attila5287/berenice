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
            ])

    dest_id = SelectField(
        choices=[('0', 'Alabama'),('1', 'Baltimore'),
                 ('2', 'California'), ('3', 'Delaware'), ('4', 'Exeter')])
    ship_status = SelectField(
        choices=[
            ('0', 'shipped'),
            ('1', 'waiting'),
            ('2', 'arrived'),
        ]
    )


class ItemDemo():
    pass
    date_posted = '07-03-2020'

    def __init__(self, make='', model='', year='', bodyType='', destId='', shipStatus=''):
        pass
        self.make = make
        self.model = model
        self.year = year
        self.bodyType = bodyType
        self.destId =destId
        self.shipStatus = shipStatus


    def __repr__(self):
        return f"ItemDemo('\n...{self.make}'\n\t '{self.model}' \n\t '{self.year}')"

