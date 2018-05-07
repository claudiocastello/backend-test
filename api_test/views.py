import requests as python_requests

from flask import abort, render_template, redirect, url_for, flash, request as flask_request

from . import app
from .forms import TestAPIForm


### Views ###

@app.route('/', methods=['GET', 'POST'])
def search():
    # Instantiate the form object
    form = TestAPIForm()

    # Load the .json with cities in the job openings in the API
    # and presents them in the dropdown menu in the search interface
    cities_url = 'http://localhost:5000/catho/api/v1.0/cities'
    city_list = python_requests.get(cities_url).json()

    if form.validate_on_submit():
        if flask_request.method == 'POST':
            query = flask_request.form.get('query_words')
            city = 'Testing'    # Need to find a way to get city from the dropdown menu
            crescent_order='False'

            URL = 'http://localhost:5000/catho/api/v1.0/search/'
            form_data = {
                        'query': query,
                        'city': city,
                        'crescent_order': crescent_order
                        }
            query_request = python_requests.get(url=URL, params=form_data)
            return redirect(query_request.url)
    return render_template('index.html', form=form, cities=city_list)
