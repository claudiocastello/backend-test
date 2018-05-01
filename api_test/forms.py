from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TestAPIForm(FlaskForm):
    '''
    Simple Form to test the API
    '''
    test_api =  StringField('Search',
                validators=[DataRequired(message='Search something...')],
                description={'placeholder': 'Search'})
