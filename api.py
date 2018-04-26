import json
from flask import Flask, jsonify

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

with open('vagas.json', 'r', encoding='utf-8') as f:
    vagas = json.load(f)


@api.route('/catho/api/v1.0/vagas', methods=['GET'])
def get_vagas():
    return jsonify(vagas)


@api.route('/catho/api/v1.0/vagas/by-salary/<int:salary>', methods=['GET'])
def get_vaga_by_salary(salary):
    vaga = [vaga for vaga in vagas['docs'] if vaga['salario'] == salary]
    if len(vaga) == 0:
        abort(404)
    return jsonify(vaga)

#
if __name__ == '__main__':
    api.run(debug=True)
