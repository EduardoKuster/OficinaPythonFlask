from config import *
from modelo import Carro
from flask import jsonify
from flask import request
import flask

@app.route("/")
def inicio():
    return '<h3>Sistema de cadastro de carros(futuro de oficina pra AV4). </h3> </br>'+\
        '<a href="/listarCarros">Listar com front end</a> </br>'+\
        '<a href="/listarCarrosJson">Listar todos os carros em json</a>'


@app.route("/listarCarrosJson")
def listarCarrosJson():
    carrosBD = db.session.query(Carro).all()
    carrosJson = []
    for x in carrosBD:
        carrosJson.append(x.json())
    resposta = jsonify(carrosJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

#rotas
@app.route("/listarCarros")
def renderizarLista():
    return flask.render_template('listarCarros.html')    

@app.route("/listagemCarros.js")#rota para carregar o js do front end
def javascriptcarros():
    return flask.render_template('listagemCarros.js')  

# iniciar o servidor web(endereço http://localhost:5000/ ou ver no terminal)
app.run(debug=True)    