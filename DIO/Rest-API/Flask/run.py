from flask import Flask
app = Flask(__name__)

@app.route("/<numero>", methods=['POST','GET'])
def Ola(numero):
    return f'Ola Mundo {numero}'

if __name__ == "__main__" :
    app.run()