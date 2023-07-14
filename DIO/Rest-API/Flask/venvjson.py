from flask import Flask, jsonify, request
import json
import uuid
app = Flask(__name__)
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

# retorna o dev pelo id, deleta, informa e edita os devs
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if res.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            msg = f'Dev do ID {id} nao existe'
            response = ({'status' : 'erro', 'message' : msg})
        except Exception:
            msg = 'Erro desconhecido'
            response = ({'status' : 'erro', 'message' : msg})
        return jsonify(response)
    elif res.method == 'PUT':
        dados = json.loads(res.data)
        devs[id] = dados
        return jsonify(dados)
    elif res.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status' : 'sucesso','message': 'Registro Excluido'})

@app.route('/dev/', methods=['POST','GET'])
def list_dev():
    if res.method == 'POST':
        dados = json.loads(res.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        return jsonify(devs[pos])
    elif res.method == 'GET':
        return jsonify(devs)

if __name__ == "__main__" :
    app.run()