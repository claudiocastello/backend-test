from flask import request, abort, render_template, redirect, url_for, flash

from . import app

from .forms import TestAPIForm


### Views ###


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestAPIForm()
    if form.validate_on_submit():
        return redirect('http://localhost:5000/catho/app/v1.0/vagas')
    return render_template('index.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
