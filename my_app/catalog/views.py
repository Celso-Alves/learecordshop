import json

from flask import request, Blueprint,  abort
from flask_restful import Resource, reqparse

from sqlalchemy.orm.util import join


from my_app import db,  api, cache
from my_app.catalog.models import Clientes, Discos, Pedidos
from datetime import datetime
from flask_restful import inputs



catalog = Blueprint('catalog', __name__)



def dt_parser(dt):
    if isinstance(dt, datetime):
        return dt.isoformat()




parser_disco = reqparse.RequestParser()
parser_disco.add_argument('nme_disco', type=str)
parser_disco.add_argument('artista', type=str)
parser_disco.add_argument('estilo', type=str)
parser_disco.add_argument('ano_lancto', type=int)
parser_disco.add_argument('quantidade', type=int)

 

class DiscoApi(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self, id_disco=None, page=1):
        
        nme_disco = request.args.get('nme_disco')
        estilo = request.args.get('estilo')
        artista = request.args.get('artista')
        ano_lancto = request.args.get('ano_lancto')

        
        #Sem id_disco, sem parametros de busca
        if not id_disco and len(request.args)==0:

            discos = Discos.query.paginate(page, 10).items
        elif len(request.args)!=0 and not id_disco:
            discos = Discos.query
            if nme_disco:
                discos = discos.filter(Discos.nme_disco.like('%' + nme_disco + '%'))
            if estilo:
                discos = discos.filter(Discos.estilo.like('%' + estilo + '%'))
            if artista:
                discos = discos.filter(Discos.artista.like('%' + artista + '%'))
            if ano_lancto:
                discos = discos.filter(Discos.ano_lancto == ano_lancto)
        else:
            discos = [Discos.query.get(id_disco)]


        if any(x is None for x in discos):
            abort(404,'Disco nao localizado pelo ID informado')

       
        res = {}
        for disco in discos:
                res[disco.id_disco] = {
                'nme_disco': disco.nme_disco,
                'artista': disco.artista,
                'estilo': disco.estilo,
                'ano_lancto': disco.ano_lancto,
                'quantidade': disco.quantidade

                }
        json_data = json.dumps(res)
        return json.loads(json_data)        



    def post(self):
        args = parser_disco.parse_args()
        nme_disco = args['nme_disco']
        artista = args['artista']
        estilo = args['estilo']
        ano_lancto = args['ano_lancto']
        quantidade = args['quantidade']
        disco = Discos(nme_disco,artista,estilo,ano_lancto,quantidade)
        db.session.add(disco)
        db.session.commit()
        res = {}
        res[disco.id_disco] = {
            'nme_disco': disco.nme_disco,
            'artista': disco.artista,
            'estilo': disco.estilo,
            'ano_lancto': disco.ano_lancto,
            'quantidade': disco.quantidade

        }
        json_data = json.dumps(res)
        return json.loads(json_data)


    
    def put(self, id_disco):
        args = parser_disco.parse_args()
        nme_disco = args['nme_disco']
        artista = args['artista']
        estilo = args['estilo']
        ano_lancto = args['ano_lancto']
        quantidade = args['quantidade']
        Discos.query.filter_by(id_disco=id_disco).update({
            'nme_disco': nme_disco,
            'artista': artista,
            'estilo':  estilo,
            'ano_lancto':  ano_lancto,
            'quantidade': quantidade
             })
        db.session.commit()
        disco = Discos.query.filter_by(id_disco=id_disco).first()
        if not disco:
            abort(404,'Disco nao localizado pelo ID informado')

        



        res = {}
        res[disco.id_disco] = {
            'nme_disco': disco.nme_disco,
            'artista': disco.artista,
            'estilo': disco.estilo,
            'ano_lancto': disco.ano_lancto,
            'quantidade': disco.quantidade
        }
        json_data = json.dumps(res)
        return json.loads(json_data)
    
    def patch(self,id_disco):
        args = parser_disco.parse_args()
                
        discos = Discos.query.filter_by(id_disco=id_disco).first()
        if not discos:
            abort(404,'Disco nao localizado pelo ID informado')
        
        if args['nme_disco']:
            discos.nme_disco = args['nme_disco']

        if args['artista']:
            discos.artista = args['artista']
        
        if args['estilo']:
            discos.estilo = args['estilo']
        
        if args['ano_lancto']:
            discos.ano_lancto = args['ano_lancto']
        
        if args['quantidade']:
            discos.quantidade = args['quantidade']

        #discos.update
        db.session.commit()
        res = {}
        res[discos.id_disco] = {
            'nme_disco': discos.nme_disco,
            'artista': discos.artista,
            'estilo': discos.estilo,
            'ano_lancto': discos.ano_lancto,
            'quantidade': discos.quantidade
        }
        json_data = json.dumps(res)
        return json.loads(json_data)        

    
    def delete(self, id_disco):

        disco = Discos.query.filter(Discos.id_disco == id_disco).one_or_none()
        if disco is None:
            return abort(404,'Disco nao localizado pelo ID informado')
        disco.delete()
        db.session.commit()
        res = {'response': 'Success'}
        json_data = json.dumps(res)
        return json.loads(json_data)

api.add_resource(
    DiscoApi,
    '/api/discos',
    '/api/discos/<int:id_disco>',
    '/api/discos/<int:id_disco>/<int:page>'
)

parser_cliente = reqparse.RequestParser()
parser_cliente.add_argument('nme_cliente', type=str)
parser_cliente.add_argument('email', type=str)
parser_cliente.add_argument('telefone', type=str)
parser_cliente.add_argument('dt_nasc', type=inputs.datetime_from_iso8601)
parser_cliente.add_argument('quantidade', type=int)
parser_cliente.add_argument('ativo', type=bool)
parser_cliente.add_argument('nr_documento', type=str)



class ClientesApi(Resource):
    def get(self, id_cliente=None, page=1):

        if not id_cliente:
            clientes = Clientes.query.paginate(page, 10).items
        else:
            clientes = [Clientes.query.get(id_cliente)]

        if any(x is None for x in clientes):
            return abort(404,'Cliente nao localizado pelo ID informado')

        res = {}
        for cliente in clientes:
                res[cliente.id_cliente] = {
                'nme_cliente': cliente.nme_cliente,
                'email': cliente.email,
                'telefone': cliente.telefone,
                'dt_nasc': dt_parser(cliente.dt_nasc),
                'ativo': cliente.ativo,
                'nr_documento': cliente.nr_documento

                }
        json_data = json.dumps(res)
        return json.loads(json_data)
    

    def post(self):
        args = parser_cliente.parse_args()
        nme_cliente = args['nme_cliente']
        email = args['email']
        telefone = args['telefone']
        dt_nasc = args['dt_nasc']
        ativo = args['ativo']
        nr_documento = args['nr_documento']

        cliente = Clientes(nme_cliente,email,telefone,dt_nasc,ativo,nr_documento)
        db.session.add(cliente)
        db.session.commit()
        res = {}
        res[cliente.id_cliente] = {
            'nme_cliente': cliente.nme_cliente,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'dt_nasc': dt_parser(cliente.dt_nasc),
            'ativo': cliente.ativo,
            'nr_documento': cliente.nr_documento
            }
        json_data = json.dumps(res)
        return json.loads(json_data)

    
    def patch(self,id_cliente):
        args = parser_cliente.parse_args()

        cliente = Clientes.query.filter_by(id_cliente=id_cliente).first()
        if not cliente:
            return json.dumps({'resposta': 'Erro Cliente nao localizado pelo ID informado'})
        
        if args['nme_cliente']:
            cliente.nme_cliente = args['nme_cliente']

        if args['email']:
            cliente.email = args['email']
        
        if args['telefone']:
            cliente.telefone = args['telefone']
        
        if args['dt_nasc']:
            cliente.dt_nasc = args['dt_nasc']
        
        if args['ativo']:
            cliente.ativo = args['ativo']
        
        if args['nr_documento']:
            cliente.nr_documento = args['nr_documento']



        db.session.commit()
        res = {}
        res[cliente.id_cliente] = {
            'nme_cliente': cliente.nme_cliente,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'dt_nasc': dt_parser(cliente.dt_nasc),
            'ativo': cliente.ativo,
            'nr_documento': cliente.nr_documento
        }
        json_data = json.dumps(res)
        return json.loads(json_data)


    def delete(self, id_cliente):
        
        cliente = Clientes.query.filter(Clientes.id_cliente == id_cliente).one_or_none()
        if cliente is None:
            return json.dumps({'resposta': 'Erro Cliente nao localizado pelo ID informado'})
        
        cliente.ativo = False
        db.session.commit()
        return json.dumps({'resposta': 'Cliente inativado com sucesso'})


api.add_resource(
    ClientesApi,
    '/api/clientes',
    '/api/clientes/<int:id_cliente>',
    '/api/clientes/<int:id_cliente>/<int:page>'
)






parser_pedido = reqparse.RequestParser()
parser_pedido.add_argument('id_disco', type=int)
parser_pedido.add_argument('quantidade', type=int)
parser_pedido.add_argument('id_cliente', type=int)
parser_pedido.add_argument('dt_pedido', type=inputs.datetime_from_iso8601)
parser_pedido.add_argument('nme_cliente',  type=str)
parser_pedido.add_argument('dt_ini', type=inputs.datetime_from_iso8601)
parser_pedido.add_argument('dt_fim', type=inputs.datetime_from_iso8601)



class PedidosApi(Resource):
    
    def get(self, id_pedido=None, page=1):


        nme_cliente = request.args.get('nme_cliente')
        dt_ini = request.args.get('dt_ini')
        dt_fim = request.args.get('dt_fim')


         #Sem id_disco, sem parametros de busca
        if not id_pedido and len(request.args)==0:
            pedidos = Pedidos.query.paginate(page, 10).items
        elif len(request.args)!=0 and not id_pedido:
            
            if dt_ini and not dt_fim:
                abort(422,'Parametro dt_fim não preenchido')

            
            if nme_cliente and dt_ini and dt_fim:
                pedidos =  db.session.query(Pedidos).join(Clientes).filter(Clientes.nme_cliente.like('%' + nme_cliente + '%'))\
                    .filter(Pedidos.dt_pedido <= dt_fim)\
                        .filter(Pedidos.dt_pedido >= dt_ini)

            if nme_cliente and not dt_ini and not dt_fim:
                pedidos =  db.session.query(Pedidos).join(Clientes).filter(Clientes.nme_cliente.like('%' + nme_cliente + '%'))
            
            if not nme_cliente and dt_ini and dt_fim:
                pedidos =  db.session.query(Pedidos).filter(Pedidos.dt_pedido <= dt_fim)\
                    .filter(Pedidos.dt_pedido >= dt_ini)
        else:
            pedidos = [Pedidos.query.get(id_pedido)]



        if any(x is None for x in pedidos):
            abort(404,'Pedido nao localizado pelo ID informado')
         
        
        
        res = {}
        for pedido in pedidos:
                res[pedido.id_pedido] = {
                'id_disco': pedido.id_disco,
                'quantidade': pedido.quantidade,
                'id_cliente': pedido.id_cliente,
                'dt_pedido': dt_parser(pedido.dt_pedido),
                'nme_disco': pedido.discos.nme_disco,
                'nme_cliente': pedido.clientes.nme_cliente
                
            }
        json_data = json.dumps(res)
        return json.loads(json_data)    
        
    
    def post(self):
        args = parser_pedido.parse_args()
                
        if args['id_cliente']:
            id_cliente = args['id_cliente']

        #validar dados
        cliente = Clientes.query.filter_by(id_cliente=id_cliente,ativo=True).first()
        if not cliente:
            return json.dumps({'resposta': 'Erro Cliente nao localizado pelo ID informado ou não ativo'})
        

        if args['id_disco']:
            id_disco = args['id_disco']
        
        disco = Discos.query.filter_by(id_disco=id_disco).first()
        if not disco:
            return json.dumps({'resposta': 'Disco não encontrado'})
        #guardar quantidade em estoque
        qtd_estoque = disco.quantidade
        #Disco encontrado
        #validar quantidade
        if args['quantidade']:
            quantidade = args['quantidade']
        else:
            quantidade = 0
                   
        if quantidade<=0:
            res = {'resposta': 'Quantidade não pode ser igual ou menor que zero'}
            json_data = json.dumps(res)
            return json.loads(json_data)

            
        
        #verificar se a quantidade solicitada está disponivel no estoque 
        #caso esteja faz a baixa, caso não esteja envia colaca num lista de espera para ser informado quando 
        #houver em estoque
        if quantidade>qtd_estoque:
            msg_estoque = u'Infelismente esse disco acabou :( , mas não se preocupe, vamos incluir seu nome na lista de espera' \
                + ',assim que estiver disponivel te informamos por e-mail.'
            return json.dumps({'resposta': msg_estoque },ensure_ascii=False)
            
            

        #tem quantidade, baixar do estoque
        disco.quantidade = qtd_estoque-quantidade
        db.session.commit()
        args['dt_pedido'] = datetime.now()
        dt_pedido = args['dt_pedido'] 
        

        #incluir o pedido
        pedido = Pedidos(id_disco=id_disco,quantidade=quantidade,id_cliente=id_cliente,dt_pedido=dt_pedido)
              

        db.session.add(pedido)
        db.session.commit()
        res = {}
        res[pedido.id_pedido] = {
            'id_disco': pedido.id_disco,
            'quantidade': pedido.quantidade,
            'id_cliente': pedido.id_cliente,
            'dt_pedido': dt_parser(pedido.dt_pedido)
                        
            }
        json_data = json.dumps(res)
        return json.loads(json_data)    
        


        



    
api.add_resource(
    PedidosApi,
    '/api/pedidos',
    '/api/pedidos/<int:id_pedido>',
    '/api/pedidos/<int:id_pedido>/<int:page>'
)    

