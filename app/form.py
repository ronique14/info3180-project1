from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class PropertyForm(FlaskForm):
  title  = StringField('title', validators=[DataRequired('A title is required.')])
  bedrooms  = StringField('bedrooms', validators=[DataRequired('A number of bedrooms is required.')])
  bathrooms  = StringField('bathrooms', validators=[DataRequired('A number of bathrooms is required.')])
  location = StringField('location', validators=[DataRequired('A location is required.')])
  price = StringField('price', validators=[DataRequired('A price is required.')])
  description = TextAreaField('description', validators=[DataRequired('A message is required.')])
  send = SubmitField('add property')
