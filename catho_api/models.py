from . import app, db, whooshee


@whooshee.register_model('title_norm') # Testing with 'title' only
class Jobs(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salario = db.Column(db.Float)
    cidade = db.Column(db.String(50), nullable=False)
    cidade_formated = db.Column(db.String(50), nullable=False)

    title_norm = db.Column(db.String(80), nullable=False)
    description_norm = db.Column(db.Text, nullable=False)

    @property
    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'salario': self.salario,
                'cidade': [self.cidade],
                'cidadeFormated': [self.cidade_formated],
                }

    def __repr__(self):
        return '({id}, {title}, {salario}, {cidade})'.format(id=self.id,
                                                             title=self.title,
                                                             salario=self.salario,
                                                             cidade=self.cidade,
                                                             description_norm=self.description_norm
                                                             )
