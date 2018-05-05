import json
from flask import jsonify, abort, url_for, redirect
from flask import request as flask_request

from . import app, db
from .models import Vagas

from .utils import normalize_text

## Loading .json file ##
with open('vagas.json', 'r', encoding='utf-8') as f:
    vagas = json.load(f)


db.drop_all()
db.create_all()

for vaga in vagas['docs']:
    vaga_to_add = Vagas(title=vaga['title'],
                        description=vaga['description'],
                        salario=vaga['salario'],
                        cidade=vaga['cidade'][0],
                        cidade_formated=vaga['cidadeFormated'][0],
                        title_norm=normalize_text(vaga['title']),
                        description_norm=normalize_text(vaga['description']),
                        cidade_norm=normalize_text(vaga['cidade'][0]))
    db.session.add(vaga_to_add)

db.session.commit()


### Views ###

# Return all entries of the .json file
@app.route('/catho/api/v1.0/vagas', methods=['GET'])
def get_vagas():
    return jsonify(vagas)


@app.route('/catho/api/v1.0/search/', methods=['GET'])
def search_vaga():
    query_words = flask_request.args.get('query')
    city = flask_request.args.get('city')
    crescent_order = flask_request.args.get('crescent_order')

    norm_words = normalize_text(query_words)
    vagas = Vagas.query.whooshee_search(norm_words, order_by_relevance=0).order_by(Vagas.salario.desc()).all()
    vagas_to_show = [vaga.serialize for vaga in vagas]
    if len(vagas_to_show) == 0:
        abort(404)
    return jsonify(vagas_to_show)

if __name__ == '__main__':
    app.run(debug=True)
