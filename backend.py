from config import *
from modelo import Baia, Carro, Endereco, Funcionario, Local, Modelo, Peca, Servico
from modelo import Plano
from modelo import Cliente
from flask import jsonify
from flask import request
import flask

@app.route("/")
def inicio():
    return flask.render_template('oficina.html')  #ir direto pra ação na página home


@app.route("/listarCarrosJson")
def listarCarrosJson():
    carrosBD = db.session.query(Carro).all()
    carrosJson = []
    for x in carrosBD:
        carrosJson.append(x.json())
    resposta = jsonify(carrosJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarClientesJson")
def listarClientesJson():
    BD = db.session.query(Cliente).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarModelosJson")
def listarModelosJson():
    BD = db.session.query(Modelo).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarEnderecosJson")
def listarEnderecosJson():
    BD = db.session.query(Endereco).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarPlanosJson")
def listarPlanosJson():
    BD = db.session.query(Plano).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarPecasJson")
def listarPecasJson():
    BD = db.session.query(Peca).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarBaiasJson")
def listarBaiasJson():
    BD = db.session.query(Baia).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarLocaisJson")
def listarLocaisJson():
    BD = db.session.query(Local).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarFuncionariosJson")
def listarFuncionariosJson():
    BD = db.session.query(Funcionario).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarServicosJson")
def listarServicosJson():
    BD = db.session.query(Servico).all()
    json = []
    for x in BD:
        json.append(x.json())
    resposta = jsonify(json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

#rotas
@app.route("/listarCarros")
def listarCarros():
    return flask.render_template('oficina.html')    

@app.route("/scriptGeral.js")#rota para carregar o js do front end
def javascriptcarros():
    return flask.render_template('scriptGeral.js')  

@app.route("/incluir_carro", methods=['post']) 
def incluir_carro(): 
   resposta = jsonify({"resultado": "Criado com sucesso", "detalhes": "ok"}) 
   dadosnovocarro = request.get_json()
   try: 
    novocarro = Carro(**dadosnovocarro) 
    db.session.add(novocarro)
    db.session.commit() 
   except Exception as e:
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 
 
@app.route("/incluir_plano", methods=['post']) 
def incluir_plano(): 
   resposta = jsonify({"resultado": "Criado com sucesso", "detalhes": "ok"}) 
   dadosnovoplano = request.get_json()
   try: 
    novoplano = Plano(**dadosnovoplano) 
    db.session.add(novoplano)
    db.session.commit() 
   except Exception as e:
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 
 


# iniciar o servidor web(endereço http://localhost:5000/ ou ver no terminal)
app.run(debug=True)    