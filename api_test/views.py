import requests as python_requests
from flask import abort, render_template, redirect, url_for, flash
from flask import request as flask_request
from . import app
from .forms import TestAPIForm

### Views ###

# Loads the search interface page and validate
# form on submit. Call 'search' url passing
# the form data as parameter to the api.
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = TestAPIForm()
#     if form.validate_on_submit():
#         word = form.test_api.data
#         return redirect(url_for('search', words=word))
#     return render_template('index.html',form=form)


# # A scratch of the search by calling directly the
# # url of the api. TODO: improve with flask request
# @app.route('/search/<words>', methods=['GET', 'POST'])
# def search(words):
#     return redirect('http://localhost:5000/catho/api/v1.0/vagas/'+words)

# search for reaquest.dict to pass parameters
@app.route('/', methods=['GET', 'POST'])
def search():
    form = TestAPIForm()
    if form.validate_on_submit():
        if flask_request.method == 'POST':
            query = flask_request.form.get('test_api')
            city='Campinas'
            crescent_order='False'

            URL = 'http://localhost:5000/catho/api/v1.0/search/'
            form_data = {
                        'query': query,
                        'city': city,
                        'crescent_order': crescent_order
                        }

            query_request = python_requests.get(url=URL, params=form_data)

            return redirect(query_request.url)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
