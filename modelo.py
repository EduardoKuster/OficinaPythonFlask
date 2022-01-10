from config import *


class Plano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    tipo = db.Column(db.Integer)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo
        }

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    marca = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca
        }

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    numerocasa = db.Column(db.Integer)

    def json(self):
        return {
            "id": self.id,
            "rua": self.rua,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "numerocasa": self.numerocasa
        }

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    enderecoId = db.Column(db.Integer, db.ForeignKey(Endereco.id), nullable=True) 
    endereco = db.relationship("Endereco")
    planoId = db.Column(db.Integer, db.ForeignKey(Plano.id), nullable=True) 
    plano = db.relationship("Plano")

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "enderecoid": self.enderecoId,
            "endereco": self.endereco.json(),
            "planoid": self.planoId,
            "plano": self.plano.json()
        }

class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    placa = db.Column(db.String(7))
    ano = db.Column(db.String(254))
    clienteId = db.Column(db.Integer, db.ForeignKey(Cliente.id), nullable=False) 
    cliente = db.relationship("Cliente")
    modeloId = db.Column(db.Integer, db.ForeignKey(Modelo.id), nullable=False) 
    modelo = db.relationship("Modelo")

    def json(self):
        return {
            "id": self.id,
            "placa": self.placa,
            "ano": self.ano,
            "clienteId": self.clienteId,
            "cliente": self.cliente.json(),
            "modeloId": self.modeloId,
            "modelo": self.modelo.json()
        }

class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    descricao = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
        }
        
class Baia(db.Model):
    id = db.Column(db.Integer, primary_key=True)       
    carroId = db.Column(db.Integer, db.ForeignKey(Carro.id), nullable=False) 
    carro = db.relationship("Carro")
    localId = db.Column(db.Integer, db.ForeignKey(Local.id), nullable=False) 
    local = db.relationship("Local")

    def json(self):
        return {
            "id": self.id,
            "carroId": self.carroId,
            "carro": self.carro.json(),
            "localId": self.localId,
            "local": self.local.json()
        }

class Peca(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254))
    preco = db.Column(db.Float)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
        }

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254))
    preco = db.Column(db.Float)
    carroId = db.Column(db.Integer, db.ForeignKey(Carro.id), nullable=False) 
    carro = db.relationship("Carro")
    pecaId = db.Column(db.Integer, db.ForeignKey(Peca.id), nullable=False) 
    peca = db.relationship("Peca")
    funcionarioId = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False) 
    funcionario = db.relationship("Funcionario")

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "carroId": self.carroId,
            "carro": self.carro.json(),
            "pecaId": self.pecaId,
            "peca": self.peca.json(),
            "funcionarioId": self.funcionarioId,
            "funcionario": self.funcionario.json(),
        }


# pra mostrar de modo entendivel no print
    def __str__(self):
        return str(self.id)+"- "+ self.marca + ", " +\
            self.modelo + ", " + self.placa+ ", " + self.ano

# teste com valores fixos    
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    #criar e adicionar modelos
    mod1 = Modelo(nome = "Corsa", marca="Chevrolet")
    db.session.add(mod1)
    mod2 = Modelo(nome = "Parati", marca="Volkswagen")
    db.session.add(mod2)
    mod3 = Modelo(nome = "Focus", marca="Ford")
    db.session.add(mod3)
    mod4 = Modelo(nome = "Uno", marca="Fiat")
    db.session.add(mod4)

    #criar e adicionar endereços para os clientes
    end1 = Endereco(rua = "Franz volles", bairro="Itoupava Central", cidade="blumenau",numerocasa="123")
    db.session.add(end1)
    end2 = Endereco(rua = "Pedro zimmermann", bairro="Itoupavazinha", cidade="blumenau",numerocasa="452")
    db.session.add(end2)

    #criar e adicionar Planos
    plano2 = Plano(nome = "Balanceamento grátis", tipo=2)
    db.session.add(plano2)
    pl = Plano(nome = "Plano troca de óleo grátis", tipo= 1)
    db.session.add(pl)

    #criar e adicionar Clientes
    cli = Cliente(nome = "Claudio", telefone = "(47)1234-1234", endereco = end1, plano = pl)
    db.session.add(cli)
    cli1 = Cliente(nome = "Jose", telefone = "(47)1235-1235", endereco = end2, plano = plano2)
    db.session.add(cli1)

    #criar e adicionar carros
    carro = Carro(modelo = mod1, placa = "1234567", ano = "2006", clienteId =cli.id, cliente =cli)
    db.session.add(carro)
    carro1 = Carro(modelo = mod2, placa = "INT9070", ano = "2006", clienteId =cli.id, cliente =cli1)
    db.session.add(carro1)
    carro2 = Carro(modelo = mod3, placa = "SST5819", ano = "2018", clienteId =cli1.id, cliente =cli1)
    db.session.add(carro2)
    carro3 = Carro(modelo = mod4, placa = "IRS4B90", ano = "2012", clienteId =cli1.id, cliente =cli)
    db.session.add(carro3)

    #criar e adicionar peças de carros
    peca1 = Peca(preco = 120.50, nome = "pneu aro 20")
    db.session.add(peca1)
    peca2 = Peca(preco = 80.00, nome = "Vela de ignição")
    db.session.add(peca2)

    #criar e adicionar funcionários da oficina
    fun = Funcionario(nome = "Paulo")
    db.session.add(fun)

    #criar e adicionar serviços
    ser = Servico(nome = "Troca de pneu", preco = 1000.00, carro =carro, peca = peca1, funcionario = fun)
    db.session.add(ser)
    ser2 = Servico(nome = "troca da vela de ignição", preco = 200.00, carro =carro2, peca = peca2, funcionario = fun)
    db.session.add(ser2)

    #criar e adicionar local das baias
    loc = Local(descricao = "Galpão principal da Matriz")
    db.session.add(loc)

    #criar e adicionar baias onde os carros se encontram
    baia = Baia(carro = carro, local =loc)
    db.session.add(baia)
    baia1 = Baia(carro = carro1, local =loc)
    db.session.add(baia1)
    baia2 = Baia(carro = carro2, local =loc)
    db.session.add(baia2)
    baia3 = Baia(carro = carro3, local =loc)
    db.session.add(baia3)

    #enviar modificações ativas na sessão pro bd
    db.session.commit()

    print("\npeças de carros cadastrados no NOVO banco de dados:")
    for pec in db.session.query(Peca).all():
        print(pec.json())

    print("\nmodelos de carros cadastrados no NOVO banco de dados:")
    for carro in db.session.query(Modelo).all():
        print(carro.json())

    print("\nplanos cadastrados no NOVO banco de dados:")
    for plano in db.session.query(Plano).all():
        print(plano.json())

    print("\nFuncioanrios cadastrados no NOVO banco de dados:")
    for f in db.session.query(Funcionario).all():
        print(f.json())

    print("\nendereços cadastrados no NOVO banco de dados:")
    for end in db.session.query(Endereco).all():
        print(end.json())

    print("\nclientes cadastrados no NOVO banco de dados:")
    for cli in db.session.query(Cliente).all():
        print(cli.json())

    print("\nBaias dos carros cadastrados no NOVO banco de dados:")
    for ba in db.session.query(Baia).all():
        print(ba.json())

    print("\nServicos cadastrados no NOVO banco de dados:")
    for serv in db.session.query(Servico).all():
        print(serv.json())

    print("\ncarros cadastrados no NOVO banco de dados:")
    for carro in db.session.query(Carro).all():
        print(carro.json())
