from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class ItemForm(FlaskForm):
    pass
    make = StringField('make', validators=[DataRequired()], default='Ford')
    model = StringField('model', validators=[DataRequired()], default='Mustang')
    year = StringField('year', validators=[DataRequired()], default='2007')
    bodyType = SelectField(
        choices=[
            ('0', 'Sedan'),('1', 'Compact'),
            ('2', 'Coupe'), ('3', 'Pickup'),
            ('4' ,'SUV')
            ])

    destId = SelectField(
        choices=[('0', 'Alabama'),('1', 'Baltimore'),
                 ('2', 'California'), ('3', 'Delaware'), ('4', 'Exeter')])
    shipStatus = SelectField(
        choices=[
            ('0', 'shipped'),
            ('1', 'waiting'),
            ('0', 'arrived'),
        ]
    )

