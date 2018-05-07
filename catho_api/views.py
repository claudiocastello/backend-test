import json
from flask import jsonify, abort, url_for, redirect
from flask import request as flask_request

from . import app, db
from .models import Jobs

from .utils import normalize_text

## Loading .json file with job openings ##
with open('vagas.json', 'r', encoding='utf-8') as f:
    jobs = json.load(f)


db.drop_all()
db.create_all()

# Creating a set to store all cities in the .json file
city_set = set(['--'])

for job in jobs['docs']:
    job_to_add = Jobs(title=job['title'],
                      description=job['description'],
                      salario=job['salario'],
                      cidade=job['cidade'][0],
                      cidade_formated=job['cidadeFormated'][0],
                      title_norm=normalize_text(job['title']),
                      description_norm=normalize_text(job['description']),
                      cidade_norm=normalize_text(job['cidade'][0]))
    city_set.add(job['cidade'][0])
    db.session.add(job_to_add)

db.session.commit()

# Taking the city set and converting to a sorted list o cities
city_list = sorted(list(city_set))


### Views ###

# Return all entries of the .json file
@app.route('/catho/api/v1.0/jobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

@app.route('/catho/api/v1.0/cities', methods=['GET'])
def get_cities():
    return jsonify(city_list)

# Search jobs by title and description (testing only with title for now)
@app.route('/catho/api/v1.0/search/', methods=['GET'])
def search_job():
    query_words = flask_request.args.get('query')
    city = flask_request.args.get('city')
    crescent_order = flask_request.args.get('crescent_order')

    norm_words = normalize_text(query_words)
    jobs = Jobs.query.whooshee_search(norm_words, order_by_relevance=0).order_by(Jobs.salario.desc()).all()
    jobs_to_show = [job.serialize for job in jobs]
    if len(jobs_to_show) == 0:
        abort(404)
    return jsonify(jobs_to_show)
