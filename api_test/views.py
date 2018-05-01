from flask import request, abort, render_template, redirect, url_for, flash
from . import app
from .forms import TestAPIForm

### Views ###

# Loads the search interface page and validate
# form on submit. Call 'search' url passing
# the form data as parameter fo the api.
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestAPIForm()
    if form.validate_on_submit():
        word = form.test_api.data
        return redirect(url_for('search', words=word))
    return render_template('index.html',form=form)


# A scratch of the search by calling directly the
# url of the api. TODO: improve with flask request
@app.route('/search/<words>', methods=['GET', 'POST'])
def search(words):
    return redirect('http://localhost:5000/catho/app/v1.0/vagas/'+words)


if __name__ == '__main__':
    app.run(debug=True)
