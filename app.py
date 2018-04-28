import os, json
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee

app = Flask(__name__)

## Config ##
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## SQLAlchemy ##
db = SQLAlchemy(app)

## Whoshee
whooshee = Whooshee(app)


## Loading .json file ##
with open('vagas.json', 'r', encoding='utf-8') as f:
    vagas = json.load(f)


# Creating SQLAlchemy database
@whooshee.register_model('title') # Testing with 'title' only
class Vagas(db.Model):
    __tablename__ = 'vagas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salario = db.Column(db.Float)
    cidade = db.Column(db.String(50), nullable=False)
    cidade_formated = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'salario': self.salario,
                'cidade': [self.cidade],
                'cidadeFormated': [self.cidade_formated]}

    def __repr__(self):
        return '({id}, {title}, {salario}, {cidade})'.format(id=self.id,
                                                             title=self.title,
                                                             salario=self.salario,
                                                             cidade=self.cidade)


db.drop_all()
db.create_all()

for vaga in vagas['docs']:
    vaga_to_add = Vagas(title=vaga['title'],
                        description=vaga['description'],
                        salario=vaga['salario'],
                        cidade=vaga['cidade'][0],
                        cidade_formated=vaga['cidadeFormated'][0])
    db.session.add(vaga_to_add)

db.session.commit()


### Views ###

# Return all entries of the .json file
@app.route('/catho/app/v1.0/vagas', methods=['GET'])
def get_vagas():
    return jsonify(vagas)


# Return entries with salario == salary
@app.route('/catho/app/v1.0/vagas/by-salary/<int:salary>', methods=['GET'])
def get_vaga_by_salary(salary):
    vagas = Vagas.query.filter_by(salario=salary).all()
    vagas_to_show = [vaga.serialize for vaga in vagas]
    if len(vagas_to_show) == 0:
        abort(404)
    return jsonify(vagas_to_show)


# Testing the full search with the word 'motorista'
@app.route('/catho/app/v1.0/vagas/motorista', methods=['GET'])
def get_vaga_assistente():
    vagas = Vagas.query.whooshee_search('motorista', order_by_relevance=0).order_by(Vagas.salario.desc()).all()
    vagas_to_show = [vaga.serialize for vaga in vagas]
    if len(vagas_to_show) == 0:
        abort(404)
    return jsonify(vagas_to_show)


if __name__ == '__main__':
    app.run(debug=True)
