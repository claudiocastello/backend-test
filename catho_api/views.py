import json
from flask import jsonify, abort, make_response, request as flask_request
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
                      description_norm=normalize_text(job['description']))
    city_set.add(job['cidade'][0])
    db.session.add(job_to_add)

db.session.commit()

# Taking the city set and converting to a sorted list o cities
city_list = sorted(list(city_set))


### Views ###
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# Return all entries of the .json file
@app.route('/catho/api/jobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

# Making the city list available as json
@app.route('/catho/api/cities', methods=['GET'])
def get_cities():
    return jsonify(city_list)

# Search jobs by title and description (testing only with 'title' for now)
@app.route('/catho/api/search/', methods=['GET'])
def search_job():
    query_words = flask_request.args.get('query')
    city = flask_request.args.get('city')
    order = flask_request.args.get('order')

    # Defining order to show results based on salary
    salary_order = Jobs.salario.asc()
    if order == 'd':
        salary_order = Jobs.salario.desc()

    # Searching the words in the job openings
    norm_words = normalize_text(query_words)
    jobs = Jobs.query.whooshee_search(norm_words, order_by_relevance=0).order_by(salary_order).all()

    # Building a list  with job openings based on search
    jobs_to_show = [job.serialize for job in jobs]
    # Filtering the list above by city
    if city != '--':
        jobs_to_show = list(filter(lambda job: job['cidade'][0] == city, jobs_to_show))

    if len(jobs_to_show) == 0:
        return abort(404)

    return jsonify(jobs_to_show)
