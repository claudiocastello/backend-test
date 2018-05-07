from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class TestAPIForm(FlaskForm):
    '''
    Simple Form to test the API
    '''
    query_words =  StringField('search_form',
                               validators=[DataRequired(message='Search something...'),
                                           Length(min=3)],
                               description={'placeholder': 'Search'})
