from . import app, db, whooshee


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
