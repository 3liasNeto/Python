import uuid
import json
from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
res = request
devs = [
    {
        'id' : str(uuid.uuid4()),
        'nome':'Elias',
        'Habilidades':['Python','Flask']
    },
    {
        'id' : str(uuid.uuid4()),
        'nome':'Eduardo',
        'Habilidades':['Python','Django']
    }
]

class DevOps(Resource):
    def get(self,id):
        try:
            response = devs[id]
        except IndexError:
            msg = f'Dev do ID {id} nao existe'
            response = ({'status' : 'erro', 'message' : msg})
        except Exception:
            msg = 'Erro desconhecido'
            response = ({'status' : 'erro', 'message' : msg})
        return response
    def put(self, id):
        dados = json.loads(res.data)
        devs[id] = dados
        return dados
    def delete(self, id):
        devs.pop(id)
        return {'status' : 'sucesso','message': 'Registro Excluido'}
    
class ListaDev(Resource):
    def get(self):
        return devs
    def post(self):
        dados = json.loads(res.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        return devs[pos]
    
api.add_resource(DevOps, '/dev/<int:id>')
api.add_resource(ListaDev, '/dev/')

if __name__ == "__main__":
    app.run()
    