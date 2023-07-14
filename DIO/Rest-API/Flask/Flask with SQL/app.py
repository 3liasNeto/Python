from flask import Flask,request
from flask_restful import Resource, Api
from models import Peoples,Activities

app = Flask(__name__)
api = Api(app)

class People(Resource):
    def get(self, nome):
        people = Peoples.query.filter_by(nome = nome).first()
        try:
            response = {
                'nome' : people.nome,
                'idade' : people.idade,
                'id' : people.id
            }
        except AttributeError:
            response = {
                'status' : 'Error',
                'message' : 'Pessoa nao Encontrada'
            }
        return response
    
    def put(self, nome):
        people = Peoples.query.filter_by(nome = nome).first()
        dados = request.json
        if 'nome' in dados:
            people.nome = dados['nome']
        if 'idade' in dados:
            people.idade = dados['idade']
        people.save()
        response = {
            'id' : people.id,
            'nome' : people.nome,
            'idade' : people.idade
        }
        return response
    
    def delete(self, nome):
        people = Peoples.query.filter_by(nome = nome).first()
        people.delete()
        return {"Message" : "deletado com sucesso", "people" : people.nome}

class ListaPeople(Resource):
    def get(self):
        people = Peoples.query.all()
        response = [{ "id" : i.id, 'nome' : i.nome, 'idade' : i.idade} for i in people]
        return response
    
    def post(self):
        dados = request.json
        people = Peoples(nome = dados["nome"], idade = dados['idade'])
        people.save()
        response = {
            'id' : people.id,
            'nome' : people.nome,
            'idade' : people.idade
        }
        return response
    
class ListActivities(Resource):
    def get(self):
        activities = Activities.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade' : i.idade} for i in activities]
        return response
        
    def post(self):
        dados = request.json
        people = Peoples.query.filter_by(nome = dados['pessoa']).first()
        activitie = Activities(nome = dados['nome'], people = people)
        activitie.save()
        response = {
            'people' : activitie.people.nome,
            'nome' : activitie.nome,
            'id' : activitie.id
        }
        return response

api.add_resource(People, '/people/<string:nome>/')
api.add_resource(ListaPeople, '/people/')
api.add_resource(ListActivities, '/activities/')


if __name__ == '__main__':
        app.run()