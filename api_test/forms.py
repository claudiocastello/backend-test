from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

class TestAPIForm(FlaskForm):
    '''
    Simple Form to test the API
    '''
    query_words =  StringField('search_form', validators=[DataRequired(message='Search something...'), Length(min=3)], description={'placeholder': 'Search'})
    cities = SelectField('cities', validators=[DataRequired()], id='select_city')
    order = SelectField('order', validators=[DataRequired()], id='select_order', choices=[('c', 'Crescente'), ('d', 'Descrescente')])
