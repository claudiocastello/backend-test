import requests as python_requests, json

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
    form.cities.choices = [(city, city) for city in city_list]

    search_results = []

    if form.validate_on_submit():
        if flask_request.method == 'POST':
            query = flask_request.form.get('query_words')
            city = flask_request.form.get('cities')
            order = flask_request.form.get('order')

            URL = 'http://localhost:5000/catho/api/v1.0/search/'
            form_data = {
                        'query': query,
                        'city': city,
                        'order': order
                        }

            query_request = python_requests.get(url=URL, params=form_data)
            search_results = query_request.json()
            return render_template('index.html',
                                    form=form,
                                    cities=city_list,
                                    search_results=search_results)
    return render_template('index.html',
                            form=form,
                            cities=city_list,
                            search_results=search_results)
