from my_app import db
import json

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

class Discos(db.Model):
    id_disco = db.Column(db.Integer, primary_key=True)
    nme_disco = db.Column(db.String(100))
    artista = db.Column(db.String(80))
    estilo = db.Column(db.String(50))
    ano_lancto = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)



    @property
    def json(self):
        return to_json(self, self.__class__)

    def __init__(self, nme_disco, artista, estilo,ano_lancto,quantidade):
        self.nme_disco = nme_disco
        self.artista = artista
        self.estilo = estilo
        self.ano_lancto = ano_lancto
        self.quantidade = quantidade
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

        

    def __repr__(self):
        return '<Disco %d>' % self.id_disco


class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nme_cliente = db.Column(db.String(80))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(30))
    dt_nasc = db.Column(db.DateTime)
    ativo = db.Column(db.Boolean,default=True)
    nr_documento = db.Column(db.String(30))

    def __init__(self,nme_cliente,email,telefone,dt_nasc,ativo,nr_documento):
        self.nme_cliente = nme_cliente
        self.email = email
        self.telefone = telefone
        self.dt_nasc = dt_nasc
        self.ativo = ativo
        self.nr_documento = nr_documento
    
    def __repr__(self):
        return '<Cliente %d>' % self.id_cliente

        

class Pedidos(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_disco =  db.Column(db.Integer, db.ForeignKey('discos.id_disco'))
    quantidade =  db.Column(db.Integer)
    id_cliente =  db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    dt_pedido = db.Column(db.DateTime)
    

    

    discos = db.relationship(
        'Discos', backref=db.backref('pedidos', lazy='dynamic')
    )

    clientes = db.relationship(
        'Clientes', backref=db.backref('pedidos', lazy='dynamic')
    )

    def __init__(self, id_disco,quantidade,id_cliente,dt_pedido):
            
            self.id_disco = id_disco
            self.quantidade = quantidade
            self.id_cliente = id_cliente
            self.dt_pedido = dt_pedido
            

    def __repr__(self):
        return '<Pedidos %d>' % self.id_pedido






