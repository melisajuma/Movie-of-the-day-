from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class GenreForm(FlaskForm):
    name = StringField('Add a Genre', validators=[Required()])
    submit = SubmitField('Submit')